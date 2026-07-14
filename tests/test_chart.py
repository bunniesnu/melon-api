import httpx
import pytest
import respx
from typing import Any

from melon.chart import MelonClient, HOURLY_CHART_URL, CHART_REPORT_URL


class TestMelonClientGetRealtimeChart:
    """Tests for MelonClient.get_hourly_chart"""

    @respx.mock
    def test_returns_parsed_hourly_chart(self, melon_client: MelonClient, sample_chart_response: dict[str, Any]):
        route = respx.get(HOURLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_chart_response)
        )

        result = melon_client.get_realtime_chart()

        assert route.called
        assert result.status == "0"
        assert result.rank_day == "2026.07.14"
        assert result.has_more is True
        assert len(result.songs) == 1

    @respx.mock
    def test_parses_chart_song_fields(self, melon_client: MelonClient, sample_chart_response: dict[str, Any]):
        respx.get(HOURLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_chart_response)
        )

        result = melon_client.get_realtime_chart()
        song = result.songs[0]

        assert song.song_id == "37928381"
        assert song.title == "LOVE ATTACK"
        assert song.album_name == "SCENEDROME"
        assert song.current_rank == 1
        assert song.past_rank == 1
        assert song.rank_gap == 0
        assert song.rank_type == "NONE"
        assert song.is_rising is False
        assert song.is_mv is True
        assert song.is_title_song is True

    @respx.mock
    def test_parses_artist_and_genre_lists(self, melon_client: MelonClient, sample_chart_response: dict[str, Any]):
        respx.get(HOURLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_chart_response)
        )

        result = melon_client.get_realtime_chart()
        song = result.songs[0]

        assert song.artists[0].artist_id == "3709231"
        assert song.artists[0].name == "RESCENE (리센느)"
        assert song.genres[0].genre_name == "Dance"

    @respx.mock
    def test_sends_correct_default_params(self, melon_client: MelonClient, sample_chart_response: dict[str, Any]):
        route = respx.get(HOURLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_chart_response)
        )

        melon_client.get_realtime_chart()

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))
        assert params["cpId"] == "AS40"
        assert params["cpKey"] == "14LNM3"
        assert params["pageSize"] == "100"

    @respx.mock
    def test_sends_custom_params(self, melon_client: MelonClient, sample_chart_response: dict[str, Any]):
        route = respx.get(HOURLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_chart_response)
        )

        melon_client.get_realtime_chart(page_size=50, resolution=1)

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))
        assert params["pageSize"] == "50"
        assert params["resolution"] == "1"

    @respx.mock
    def test_raises_on_http_error(self, melon_client: MelonClient):
        respx.get(HOURLY_CHART_URL).mock(return_value=httpx.Response(500))

        with pytest.raises(httpx.HTTPStatusError):
            melon_client.get_realtime_chart()


class TestMelonClientGetChartReport:
    """Tests for MelonClient.get_chart_report"""

    @respx.mock
    def test_returns_parsed_chart_report(self, melon_client: MelonClient, sample_report_response):
        route = respx.get(CHART_REPORT_URL).mock(
            return_value=httpx.Response(200, json=sample_report_response)
        )

        result = melon_client.get_chart_report(song_id="37928381")

        assert route.called
        assert result.result_code == "0"
        assert result.song_info.song_id == "37928381"
        assert result.song_info.title == "LOVE ATTACK"
        assert result.song_info.current_rank == 1

    @respx.mock
    def test_parses_nested_listener_and_rank_charts(self, melon_client: MelonClient, sample_report_response):
        respx.get(CHART_REPORT_URL).mock(
            return_value=httpx.Response(200, json=sample_report_response)
        )

        result = melon_client.get_chart_report(song_id="37928381")

        assert result.listener_data.one_hour == "-"
        assert result.rank_chart.y_maximum == 61
        assert result.yester_chart_info.first_info_value == "2위"

    @respx.mock
    def test_sends_song_id_param(self, melon_client: MelonClient, sample_report_response):
        route = respx.get(CHART_REPORT_URL).mock(
            return_value=httpx.Response(200, json=sample_report_response)
        )

        melon_client.get_chart_report(song_id="37928381")

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))
        assert params["songId"] == "37928381"

    @respx.mock
    def test_sends_default_cp_params(self, melon_client: MelonClient, sample_report_response):
        route = respx.get(CHART_REPORT_URL).mock(
            return_value=httpx.Response(200, json=sample_report_response)
        )

        melon_client.get_chart_report(song_id="37928381")

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))
        assert params["cpId"] == "AS40"
        assert params["cpKey"] == "14LNC3"
        assert params["appVer"] == "6.2.0"

    @respx.mock
    def test_raises_on_http_error(self, melon_client: MelonClient):
        respx.get(CHART_REPORT_URL).mock(return_value=httpx.Response(500))

        with pytest.raises(httpx.HTTPStatusError):
            melon_client.get_chart_report(song_id="37928381")

    @respx.mock
    def test_raises_on_404(self, melon_client: MelonClient):
        respx.get(CHART_REPORT_URL).mock(return_value=httpx.Response(404))

        with pytest.raises(httpx.HTTPStatusError):
            melon_client.get_chart_report(song_id="99999999")


class TestMelonClientContextManager:
    """Tests for context manager behavior"""

    def test_enter_returns_self(self):
        client = MelonClient()
        with client as ctx:
            assert ctx is client
        client.close()

    def test_close_closes_underlying_client(self):
        client = MelonClient()
        client.close()
        assert client.client.is_closed
