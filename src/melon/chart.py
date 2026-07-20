"""Synchronous client for Melon's chart endpoints.

Every endpoint returns an envelope whose parsed payload is in ``response``.
The methods in :class:`MelonClient` unwrap that envelope and validate it with
the matching model.
"""

import httpx
from typing import Literal
from melon.models import AlbumInfo, ArtistChart, ChartGraph, DailyChart, FiveGraph, Hot100Chart, RealtimeChart, ChartReport, Top100Chart, WeeklyChart

HOURLY_CHART_URL = "https://m.app.melon.com/chart/hourly/hourlyChartList.json"
CHART_REPORT_URL = "https://m2.melon.com/m6/chart/song/chartReport.json"
TOP100_CHART_URL = "https://m2.melon.com/m6/chart/ent/songChartList.json"
DAILY_CHART_URL = "https://m2.melon.com/m5/chart/top/daily/songChartList.json"
WEEKLY_CHART_URL = "https://m2.melon.com/m5/chart/top/weekly/songChartList.json"
HOT100_CHART_URL = "https://m2.melon.com/m6/chart/hot100/list.json"
HOT100_GRAPH_HOUR_URL = "https://m2.melon.com/m6/chart/hour/graph.json"
HOT100_GRAPH_5MIN_URL = "https://m2.melon.com/m6/chart/hour/five/graph.json"
ARTIST_CHART_URL = "https://m2.melon.com/chart/artist/artistChartList.json"
ALBUM_INFO_URL = "https://m2.melon.com/m6/v3/album/info.json"


class MelonClient:
    """Reusable synchronous HTTP client for Melon chart and chart-graph APIs."""

    def __init__(self, timeout: float = 10.0):
        """Create the underlying HTTP client with the timeout in seconds."""
        self.client = httpx.Client(timeout=timeout)

    def get_realtime_chart(
        self,
        cp_id: str = "AS40",
        cp_key: str = "14LNM3",
        version: str = "4.0",
        resolution: int = 2,
        app_ver: str = "4.1.0.1",
        os_version: str = "11",
        is_recom: str = "N",
        page_size: int = 100,
    ) -> RealtimeChart:
        """Fetch the hourly chart snapshot.

        Returns songs from ``CHARTLIST`` plus its date/time snapshot. ``page_size``
        controls the number of entries requested (100 by default).
        """
        params = {
            "cpId": cp_id,
            "cpKey": cp_key,
            "v": version,
            "resolution": resolution,
            "appVer": app_ver,
            "osVersion": os_version,
            "isRecom": is_recom,
            "pageSize": page_size,
        }
        response = self.client.get(HOURLY_CHART_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return RealtimeChart.model_validate(raw["response"])

    def get_chart_report(
        self,
        song_id: str,
        cp_id: str = "AS40",
        cp_key: str = "14LNC3",
        app_ver: str = "6.2.0",
    ) -> ChartReport:
        """Fetch the listener and rank-history report for ``song_id``."""
        params = {
            "cpId": cp_id,
            "cpKey": cp_key,
            "appVer": app_ver,
            "songId": song_id,
        }
        response = self.client.get(CHART_REPORT_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return ChartReport.model_validate(raw["response"])

    def get_top100_chart(
        self,
        cp_id: str = "IS40",
        cp_key: str = "17LNM9",
        app_ver: str = "6.22.1",
    ) -> Top100Chart:
        """Fetch the current Top 100 chart, whose songs are in ``SONGLIST``."""
        params = {
            "cpId": cp_id,
            "cpKey": cp_key,
            "appVer": app_ver,
        }
        response = self.client.get(TOP100_CHART_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return Top100Chart.model_validate(raw["response"])

    def get_daily_chart(
        self,
        cp_id: str = "IS40",
        cp_key: str = "17LNM9",
        app_ver: str = "6.22.1",
    ) -> DailyChart:
        """Fetch the daily Top 100 chart; its API may return a null rank date."""
        params = {
            "cpId": cp_id,
            "cpKey": cp_key,
            "appVer": app_ver,
        }
        response = self.client.get(DAILY_CHART_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return DailyChart.model_validate(raw["response"])

    def get_weekly_chart(
        self,
        cp_id: str = "IS40",
        cp_key: str = "17LNM9",
        app_ver: str = "6.22.1",
    ) -> WeeklyChart:
        """Fetch the weekly Top 100 chart and its weekly popularity-award data."""
        params = {
            "cpId": cp_id,
            "cpKey": cp_key,
            "appVer": app_ver,
        }
        response = self.client.get(WEEKLY_CHART_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return WeeklyChart.model_validate(raw["response"])

    def get_hot100_chart(
        self,
        chart_type: Literal["D30", "D100"] = "D100",
        cp_id: str = "IS40",
        cp_key: str = "17LNM9",
        app_ver: str = "6.22.1",
    ) -> Hot100Chart:
        """Fetch a Hot 100 snapshot for ``D30`` or ``D100`` (default)."""
        params = {
            "chartType": chart_type,
            "cpId": cp_id,
            "cpKey": cp_key,
            "appVer": app_ver,
        }
        response = self.client.get(HOT100_CHART_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return Hot100Chart.model_validate(raw["response"])

    def get_hot100_graph_hour(
        self,
        v: str = "4.0",
        cp_id: str = "IS40",
        cp_key: str = "17LNM9",
    ) -> ChartGraph:
        """Fetch the hourly Hot 100 score/rank graph series."""
        params = {
            "v": v,
            "cpId": cp_id,
            "cpKey": cp_key,
        }
        response = self.client.get(HOT100_GRAPH_HOUR_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return ChartGraph.model_validate(raw["response"])

    def get_hot100_graph_five(
        self,
        v: str = "4.0",
        cp_id: str = "IS40",
        cp_key: str = "17LNM9",
    ) -> FiveGraph:
        """Fetch the five-minute Hot 100 score graph series."""
        params = {
            "v": v,
            "cpId": cp_id,
            "cpKey": cp_key,
        }
        response = self.client.get(HOT100_GRAPH_5MIN_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return FiveGraph.model_validate(raw["response"])

    def get_artist_chart(
        self,
        page_size: int = 50,
        search_type: str = "DP0000",
        start_index: int = 1,
        v: str = "4.0",
        cp_id: str = "IS40",
        cp_key: str = "17LNM9",
        app_ver: str = "6.22.1",
    ) -> ArtistChart:
        """Fetch a paginated artist chart for the selected ``search_type``."""
        params = {
            "pageSize": page_size,
            "searchType": search_type,
            "startIndex": start_index,
            "v": v,
            "cpId": cp_id,
            "cpKey": cp_key,
            "appVer": app_ver,
        }
        response = self.client.get(ARTIST_CHART_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return ArtistChart.model_validate(raw["response"])

    def get_album_info(
        self,
        album_id: str,
        cp_id: str = "AS40",
        cp_key: str = "14LNC3",
        app_ver: str = "6.2.0",
    ) -> AlbumInfo:
        """Fetch metadata, credits, ratings, and notes for ``album_id``."""
        params = {
            "albumId": album_id,
            "cpId": cp_id,
            "cpKey": cp_key,
            "appVer": app_ver,
        }
        response = self.client.get(ALBUM_INFO_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return AlbumInfo.model_validate(raw["response"])

    def close(self):
        """Close the underlying :class:`httpx.Client`."""
        self.client.close()

    def __enter__(self):
        """Return this client for use in a ``with MelonClient()`` block."""
        return self

    def __exit__(self, *args):
        """Close the HTTP client when the context-manager block exits."""
        self.close()
