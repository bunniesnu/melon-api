import httpx
import pytest
import respx

from melon.chart import MelonClient, HOURLY_CHART_URL, CHART_REPORT_URL


class TestMelonClientGetHourlyChart:
    """Tests for MelonClient.get_hourly_chart"""

    @respx.mock
    def test_returns_parsed_json_on_success(self, melon_client, sample_chart_response):
        route = respx.get(HOURLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_chart_response)
        )

        result = melon_client.get_hourly_chart()

        assert route.called
        assert result == sample_chart_response

    @respx.mock
    def test_sends_correct_default_params(self, melon_client, sample_chart_response):
        route = respx.get(HOURLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_chart_response)
        )

        melon_client.get_hourly_chart()

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))
        assert params["cpId"] == "AS40"
        assert params["cpKey"] == "14LNM3"
        assert params["pageSize"] == "100"

    @respx.mock
    def test_sends_custom_params(self, melon_client, sample_chart_response):
        route = respx.get(HOURLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_chart_response)
        )

        melon_client.get_hourly_chart(page_size=50, resolution=1)

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))
        assert params["pageSize"] == "50"
        assert params["resolution"] == "1"

    @respx.mock
    def test_raises_on_http_error(self, melon_client):
        respx.get(HOURLY_CHART_URL).mock(return_value=httpx.Response(500))

        with pytest.raises(httpx.HTTPStatusError):
            melon_client.get_hourly_chart()

    @respx.mock
    def test_raises_on_404(self, melon_client):
        respx.get(HOURLY_CHART_URL).mock(
            return_value=httpx.Response(404)
        )

        with pytest.raises(httpx.HTTPStatusError):
            melon_client.get_hourly_chart()

class TestMelonClientGetChartReport:
    """Tests for MelonClient.get_chart_report"""

    @respx.mock
    def test_returns_parsed_json_on_success(self, melon_client, sample_report_response):
        route = respx.get(CHART_REPORT_URL).mock(
            return_value=httpx.Response(200, json=sample_report_response)
        )

        result = melon_client.get_chart_report(song_id="37928381")

        assert route.called
        assert result == sample_report_response

    @respx.mock
    def test_sends_song_id_param(self, melon_client, sample_report_response):
        route = respx.get(CHART_REPORT_URL).mock(
            return_value=httpx.Response(200, json=sample_report_response)
        )

        melon_client.get_chart_report(song_id="37928381")

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))
        assert params["songId"] == "37928381"

    @respx.mock
    def test_sends_default_cp_params(self, melon_client, sample_report_response):
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
    def test_raises_on_http_error(self, melon_client):
        respx.get(CHART_REPORT_URL).mock(return_value=httpx.Response(500))

        with pytest.raises(httpx.HTTPStatusError):
            melon_client.get_chart_report(song_id="37928381")

    @respx.mock
    def test_raises_on_404(self, melon_client):
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
