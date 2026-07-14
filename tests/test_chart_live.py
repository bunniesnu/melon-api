import pytest
from melon.chart import MelonClient


@pytest.mark.live
class TestMelonClientLive:
    """
    Integration tests that hit the real Melon API.
    Run explicitly with: uv run pytest -m live
    """

    def test_get_hourly_chart_returns_valid_response(self):
        with MelonClient() as client:
            chart = client.get_realtime_chart()

        assert len(chart.songs) > 0

    def test_chart_entries_have_expected_fields(self):
        with MelonClient() as client:
            chart = client.get_realtime_chart()

        first_song = chart.songs[0]
        assert first_song.song_id
        assert first_song.title
        assert first_song.current_rank >= 1

    def test_page_size_limits_results(self):
        with MelonClient() as client:
            chart = client.get_realtime_chart(page_size=10)

        assert len(chart.songs) <= 10

    def test_get_chart_report_returns_valid_response(self):
        with MelonClient() as client:
            chart = client.get_realtime_chart(page_size=1)
            top_song_id = chart.songs[0].song_id

            report = client.get_chart_report(song_id=top_song_id)

        assert report.song_info.song_id == top_song_id
        assert report.song_info.title

    def test_get_top100_chart_returns_valid_response(self):
        with MelonClient() as client:
            chart = client.get_top100_chart()

        assert chart.status == "0"
        assert len(chart.songs) > 0
        assert chart.songs[0].current_rank >= 1

    def test_get_daily_chart_returns_valid_response(self):
        with MelonClient() as client:
            chart = client.get_daily_chart()

        assert chart.status == "0"
        assert len(chart.songs) > 0
        assert chart.songs[0].current_rank >= 1

    def test_get_weekly_chart_returns_valid_response(self):
        with MelonClient() as client:
            chart = client.get_weekly_chart()

        assert chart.status == "0"
        assert len(chart.songs) > 0
        assert chart.songs[0].current_rank >= 1

    def test_get_hot100_chart_returns_valid_response(self):
        with MelonClient() as client:
            chart = client.get_hot100_chart("D100")

        assert chart.status == "0"
        assert len(chart.songs) > 0
        assert chart.songs[0].current_rank >= 1

        with MelonClient() as client:
            chart = client.get_hot100_chart("D30")

        assert chart.status == "0"
        assert len(chart.songs) > 0
        assert chart.songs[0].current_rank >= 1
