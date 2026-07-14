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
            songs = client.get_hourly_chart()

        assert len(songs) > 0

    def test_chart_entries_have_expected_fields(self):
        with MelonClient() as client:
            songs = client.get_hourly_chart()

        first_song = songs[0]
        assert first_song.song_id
        assert first_song.title
        assert first_song.current_rank >= 1  # rank exists and is valid, not hardcoded to 1

    def test_page_size_limits_results(self):
        with MelonClient() as client:
            songs = client.get_hourly_chart(page_size=10)

        assert len(songs) <= 10

    def test_get_chart_report_returns_valid_response(self):
        with MelonClient() as client:
            # Use whatever song is currently #1, instead of a hardcoded SONGID
            chart = client.get_hourly_chart(page_size=1)
            top_song_id = chart[0].song_id

            report = client.get_chart_report(song_id=top_song_id)

        assert report.song_info.song_id == top_song_id
        assert report.song_info.title  # non-empty
