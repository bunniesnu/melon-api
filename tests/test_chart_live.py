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
            data = client.get_hourly_chart()

        assert data["response"]["STATUS"] == "0"
        assert "CHARTLIST" in data["response"]
        assert len(data["response"]["CHARTLIST"]) > 0

    def test_chart_entries_have_expected_fields(self):
        with MelonClient() as client:
            data = client.get_hourly_chart()

        first_song = data["response"]["CHARTLIST"][0]
        assert "SONGID" in first_song
        assert "SONGNAME" in first_song
        assert "CURRANK" in first_song
        assert first_song["CURRANK"] == "1"

    def test_page_size_limits_results(self):
        with MelonClient() as client:
            data = client.get_hourly_chart(page_size=10)

        assert len(data["response"]["CHARTLIST"]) <= 10

    def test_get_chart_report_returns_valid_response(self):
        with MelonClient() as client:
            data = client.get_chart_report(song_id="37928381")

        assert data["response"]["RESULTCODE"] == "0"
        assert data["response"]["SONGINFO"]["SONGID"] == "37928381"
