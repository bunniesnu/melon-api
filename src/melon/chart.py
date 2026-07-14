import httpx
from melon.models import HourlyChart, ChartReport

HOURLY_CHART_URL = "https://m.app.melon.com/chart/hourly/hourlyChartList.json"
CHART_REPORT_URL = "https://m2.melon.com/m6/chart/song/chartReport.json"


class MelonClient:
    def __init__(self, timeout: float = 10.0):
        self.client = httpx.Client(timeout=timeout)

    def get_hourly_chart(
        self,
        cp_id: str = "AS40",
        cp_key: str = "14LNM3",
        version: str = "4.0",
        resolution: int = 2,
        app_ver: str = "4.1.0.1",
        os_version: str = "11",
        is_recom: str = "N",
        page_size: int = 100,
    ) -> HourlyChart:
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
        return HourlyChart.model_validate(raw["response"])

    def get_chart_report(
        self,
        song_id: str,
        cp_id: str = "AS40",
        cp_key: str = "14LNC3",
        app_ver: str = "6.2.0",
    ) -> ChartReport:
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

    def close(self):
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
