import httpx
import pytest
import respx
from typing import Any

from melon.chart import DAILY_CHART_URL, HOT100_CHART_URL, HOT100_GRAPH_HOUR_URL, TOP100_CHART_URL, WEEKLY_CHART_URL, MelonClient, HOURLY_CHART_URL, CHART_REPORT_URL


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


class TestMelonClientGetTop100Chart:
    """Tests for MelonClient.get_top100_chart"""

    @respx.mock
    def test_returns_parsed_top100_chart(self, melon_client: MelonClient, sample_top100_response):
        route = respx.get(TOP100_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_top100_response)
        )

        result = melon_client.get_top100_chart()

        assert route.called
        assert result.status == "0"
        assert result.rank_day == "2026.07.14"
        assert len(result.songs) == 1

    @respx.mock
    def test_parses_top100_song_fields(self, melon_client: MelonClient, sample_top100_response):
        respx.get(TOP100_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_top100_response)
        )

        result = melon_client.get_top100_chart()
        song = result.songs[0]

        assert song.song_id == "37928381"
        assert song.title == "LOVE ATTACK"
        assert song.current_rank == 1
        assert song.genres[0].genre_name == "댄스"

    @respx.mock
    def test_sends_correct_default_params(self, melon_client: MelonClient, sample_top100_response):
        route = respx.get(TOP100_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_top100_response)
        )

        melon_client.get_top100_chart()

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))
        assert params["cpId"] == "IS40"
        assert params["cpKey"] == "17LNM9"
        assert params["appVer"] == "6.22.1"

    @respx.mock
    def test_raises_on_http_error(self, melon_client: MelonClient):
        respx.get(TOP100_CHART_URL).mock(return_value=httpx.Response(500))

        with pytest.raises(httpx.HTTPStatusError):
            melon_client.get_top100_chart()


class TestMelonClientGetDailyChart:
    """Tests for MelonClient.get_daily_chart"""

    @respx.mock
    def test_returns_parsed_daily_chart(self, melon_client: MelonClient, sample_daily_response):
        route = respx.get(DAILY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_daily_response)
        )

        result = melon_client.get_daily_chart()

        assert route.called
        assert result.status == "0"
        assert len(result.songs) == 1

    @respx.mock
    def test_parses_daily_song_fields(self, melon_client: MelonClient, sample_daily_response):
        respx.get(DAILY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_daily_response)
        )

        result = melon_client.get_daily_chart()
        song = result.songs[0]

        assert song.song_id == "37928381"
        assert song.title == "LOVE ATTACK"
        assert song.current_rank == 1
        assert song.genres[0].genre_name == "댄스"

    @respx.mock
    def test_sends_correct_default_params(self, melon_client: MelonClient, sample_daily_response):
        route = respx.get(DAILY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_daily_response)
        )

        melon_client.get_daily_chart()

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))
        assert params["cpId"] == "IS40"
        assert params["cpKey"] == "17LNM9"
        assert params["appVer"] == "6.22.1"

    @respx.mock
    def test_raises_on_http_error(self, melon_client: MelonClient):
        respx.get(DAILY_CHART_URL).mock(return_value=httpx.Response(500))

        with pytest.raises(httpx.HTTPStatusError):
            melon_client.get_daily_chart()


class TestMelonClientGetWeeklyChart:
    """Tests for MelonClient.get_weekly_chart"""

    @respx.mock
    def test_returns_parsed_weekly_chart(self, melon_client: MelonClient, sample_weekly_response):
        route = respx.get(WEEKLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_weekly_response)
        )

        result = melon_client.get_weekly_chart()

        assert route.called
        assert result.status == "0"
        assert result.start_day == "20260706"
        assert result.end_day == "20260712"
        assert result.has_more is False
        assert len(result.songs) == 3

    @respx.mock
    def test_parses_weekly_song_fields(self, melon_client: MelonClient, sample_weekly_response):
        respx.get(WEEKLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_weekly_response)
        )

        result = melon_client.get_weekly_chart()
        song = result.songs[0]

        assert song.song_id == "602024048"
        assert song.title == "갑자기"
        assert song.album_name == "I.O.I 3rd MINI ALBUM [I.O.I : LOOP]"
        assert song.current_rank == 1
        assert song.past_rank == 1
        assert song.rank_gap == 0
        assert song.rank_type == "NONE"
        assert song.is_rising is False
        assert song.is_mv is True
        assert song.is_title_song is True

    @respx.mock
    def test_parses_music_award(self, melon_client: MelonClient, sample_weekly_response):
        respx.get(WEEKLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_weekly_response)
        )

        result = melon_client.get_weekly_chart()

        award = result.music_award

        assert award.title == "주간 인기상 투표"
        assert award.award_year == 2026
        assert award.award_month == 7
        assert award.award_week == 2
        assert award.week_status == "P"
        assert len(award.week_rank_list) == 3

    @respx.mock
    def test_parses_weekly_award_entry(self, melon_client: MelonClient, sample_weekly_response):
        respx.get(WEEKLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_weekly_response)
        )

        result = melon_client.get_weekly_chart()

        entry = result.music_award.week_rank_list[0]

        assert entry.current_rank == 1
        assert entry.song_name == "Pretty Girl"
        assert entry.artist_id == "3709231"
        assert entry.artist_name == "RESCENE (리센느)"
        assert entry.vote_percent == 39
        assert entry.start_month == 7
        assert entry.start_week == 3

    @respx.mock
    def test_sends_correct_default_params(self, melon_client: MelonClient, sample_weekly_response):
        route = respx.get(WEEKLY_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_weekly_response)
        )

        melon_client.get_weekly_chart()

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))

        assert params["cpId"] == "IS40"
        assert params["cpKey"] == "17LNM9"
        assert params["appVer"] == "6.22.1"

    @respx.mock
    def test_raises_on_http_error(self, melon_client: MelonClient):
        respx.get(WEEKLY_CHART_URL).mock(
            return_value=httpx.Response(500)
        )

        with pytest.raises(httpx.HTTPStatusError):
            melon_client.get_weekly_chart()


class TestMelonClientGetHot100Chart:
    """Tests for MelonClient.get_hot100_chart"""

    @respx.mock
    def test_returns_parsed_hot100_chart(self, melon_client: MelonClient, sample_hot100_response):
        route = respx.get(HOT100_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_hot100_response)
        )

        result = melon_client.get_hot100_chart()

        assert route.called
        assert result.status == "0"
        assert result.rank_day == "2026.07.14"
        assert result.rank_hour == "14:00"
        assert len(result.songs) == 1

    @respx.mock
    def test_parses_hot100_song_fields(self, melon_client: MelonClient, sample_hot100_response):
        respx.get(HOT100_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_hot100_response)
        )

        result = melon_client.get_hot100_chart()
        song = result.songs[0]

        assert song.song_id == "602024048"
        assert song.title == "갑자기"
        assert song.album_name == "I.O.I 3rd MINI ALBUM [I.O.I : LOOP]"
        assert song.current_rank == 1
        assert song.past_rank == 1
        assert song.rank_gap == 0
        assert song.rank_type == "NONE"
        assert song.is_rising is False
        assert song.is_mv is True
        assert song.is_title_song is True

    @respx.mock
    def test_parses_artist_and_genre_lists(self, melon_client: MelonClient, sample_hot100_response):
        respx.get(HOT100_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_hot100_response)
        )

        result = melon_client.get_hot100_chart()
        song = result.songs[0]

        assert song.artists[0].artist_id == "960251"
        assert song.artists[0].name == "아이오아이 (I.O.I)"

        assert len(song.genres) == 2
        assert song.genres[0].genre_name == "댄스"
        assert song.genres[1].genre_name == "아이돌"

    @respx.mock
    def test_parses_chart_metadata(self, melon_client: MelonClient, sample_hot100_response):
        respx.get(HOT100_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_hot100_response)
        )

        result = melon_client.get_hot100_chart()

        assert result.chart_info.link_type == "ZA"
        assert result.chart_info.link_url.endswith("hot100ChartInfo.htm")
        assert result.menu_id == "1000003084"
        assert result.page == "멜론차트_HOT100"

    @respx.mock
    def test_sends_correct_default_params(self, melon_client: MelonClient, sample_hot100_response):
        route = respx.get(HOT100_CHART_URL).mock(
            return_value=httpx.Response(200, json=sample_hot100_response)
        )

        melon_client.get_hot100_chart()

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))

        assert params["cpId"] == "IS40"
        assert params["cpKey"] == "17LNM9"
        assert params["appVer"] == "6.22.1"

    @respx.mock
    def test_raises_on_http_error(self, melon_client: MelonClient):
        respx.get(HOT100_CHART_URL).mock(
            return_value=httpx.Response(500)
        )

        with pytest.raises(httpx.HTTPStatusError):
            melon_client.get_hot100_chart()


class TestMelonClientGetHot100GraphHour:
    """Tests for MelonClient.get_hot100_graph"""

    @respx.mock
    def test_returns_parsed_hot100_graph(self, melon_client: MelonClient, sample_hot100_graph_hour_response):
        route = respx.get(HOT100_GRAPH_HOUR_URL).mock(
            return_value=httpx.Response(200, json=sample_hot100_graph_hour_response)
        )

        result = melon_client.get_hot100_graph_hour()

        assert route.called
        assert result.status == "0"
        assert len(result.graph_data_list) == 1

    @respx.mock
    def test_parses_graph_entries(self, melon_client: MelonClient, sample_hot100_graph_hour_response):
        respx.get(HOT100_GRAPH_HOUR_URL).mock(
            return_value=httpx.Response(200, json=sample_hot100_graph_hour_response)
        )

        result = melon_client.get_hot100_graph_hour()

        entry = result.graph_data_list[0]
        point = entry.graph_data[0]

        assert entry.song_id == "602450078"
        assert entry.graph_rank == 1
        assert point.x == 0
        assert point.value == 4.607

    @respx.mock
    def test_sends_correct_params(self, melon_client: MelonClient, sample_hot100_graph_hour_response):
        route = respx.get(HOT100_GRAPH_HOUR_URL).mock(
            return_value=httpx.Response(200, json=sample_hot100_graph_hour_response)
        )

        melon_client.get_hot100_graph_hour()

        request = route.calls[0].request
        params = dict(httpx.QueryParams(request.url.query))

        assert params["v"] == "4.0"
        assert params["cpId"] == "IS40"
        assert params["cpKey"] == "17LNM9"

    @respx.mock
    def test_raises_on_http_error(self, melon_client: MelonClient):
        respx.get(HOT100_GRAPH_HOUR_URL).mock(
            return_value=httpx.Response(500)
        )

        with pytest.raises(httpx.HTTPStatusError):
            melon_client.get_hot100_graph_hour()