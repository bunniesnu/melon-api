import pytest
from melon import MelonClient


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

    def test_get_chart_report_invalid_song_id_returns_None(self):
        with MelonClient() as client:
            assert client.get_chart_report(song_id="34491913") is None

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

    def test_get_hot100_graph_hour_returns_valid_response(self):
        with MelonClient() as client:
            graph = client.get_hot100_graph_hour()

        assert graph.status == "0"
        assert len(graph.graph_data_list) > 0
        assert graph.graph_data_list[0].graph_rank >= 1
        assert graph.graph_data_list[0].graph_chart_info.current_rank >= 1

    def test_get_hot100_graph_five_returns_valid_response(self):
        with MelonClient() as client:
            graph = client.get_hot100_graph_five()

        assert graph.status == "0"
        assert len(graph.graph_data_list) > 0

        first = graph.graph_data_list[0]
        assert first.song_id
        assert first.last_group_current_score >= 0
        assert first.graph_rank >= 0
        assert first.share_value >= 0
        assert first.graph_chart_info.song_id
        assert first.graph_chart_info.title

        assert len(first.graph_data) > 0

        point = first.graph_data[0]
        assert point.x >= 0
        assert point.value >= 0

        assert len(graph.x_categories) > 0
        assert graph.five_time
        assert graph.rank_day
        assert graph.rank_hour
        assert isinstance(graph.five_error_flag, bool)

    def test_get_artist_chart_returns_valid_response(self):
        with MelonClient() as client:
            chart = client.get_artist_chart()

        assert chart.status == "0"
        assert len(chart.artists) > 0
        assert chart.artists[0].current_rank >= 1
        first_artist = chart.artists[0]
        assert first_artist.artist_id
        assert first_artist.name
        assert first_artist.total_fan_count >= 0

    def test_get_artist_songs_returns_valid_response(self):
        with MelonClient() as client:
            artist_songs = client.get_artist_songs("3709231")

        assert artist_songs.result_code == "0"
        assert isinstance(artist_songs.has_more, bool)
        assert len(artist_songs.songs) > 0

        first_song = artist_songs.songs[0]
        assert first_song.song_id
        assert first_song.title
        assert first_song.artists
        assert first_song.artists[0].artist_id == "3709231"

    def test_get_artist_albums_returns_valid_response(self):
        with MelonClient() as client:
            artist_albums = client.get_artist_albums("3709231")

        assert artist_albums.result_code == "0"
        assert isinstance(artist_albums.has_more, bool)
        assert len(artist_albums.albums) > 0

        first_album = artist_albums.albums[0]
        assert first_album.album_id
        assert first_album.album_name
        assert first_album.artist_list
        assert first_album.artist_list[0].artist_id == "3709231"

    def test_get_artist_videos_returns_valid_response(self):
        with MelonClient() as client:
            artist_videos = client.get_artist_videos("3709231")

        assert artist_videos.result_code == "0"
        assert isinstance(artist_videos.has_more, bool)
        assert len(artist_videos.videos) > 0

        first_video = artist_videos.videos[0]
        assert first_video.mv_id
        assert first_video.name
        assert first_video.song_id == "602450078"
        assert first_video.repartist.artist_id == "3709231"

    def test_get_artist_photos_returns_valid_response(self):
        with MelonClient() as client:
            artist_photos = client.get_artist_photos("3709231")

        assert artist_photos.result_code == "0"
        assert isinstance(artist_photos.has_more, bool)
        assert len(artist_photos.photos) > 0

        first_photo = artist_photos.photos[0]
        assert first_photo.photo_id
        assert first_photo.photo_img
        assert first_photo.photo_name
        assert artist_photos.artist_name == "RESCENE (리센느)"

    def test_get_artist_detail_returns_valid_response(self):
        with MelonClient() as client:
            artist_detail = client.get_artist_detail("3709231")

        assert artist_detail.result_code == "0"
        assert artist_detail.artist_id == "3709231"
        assert artist_detail.artist_name == "RESCENE (리센느)"
        assert artist_detail.debut_song.song_id
        assert artist_detail.credit_info.release_song_count >= 0

    def test_get_album_info_returns_valid_response(self):
        with MelonClient() as client:
            album_info = client.get_album_info("13788545")

        assert album_info.result_code == "0"
        assert album_info.album.album_id == "13788545"
        assert album_info.album.name
        assert len(album_info.album.artist_list) > 0
        assert album_info.album.artist_list[0].artist_id

    def test_get_album_songs_returns_valid_response(self):
        with MelonClient() as client:
            album_songs = client.get_album_songs("13788545")

        assert album_songs.result_code == "0"
        assert album_songs.total_song_count > 0
        assert len(album_songs.discs) > 0

        disc = album_songs.discs[0]
        assert len(disc.songs) > 0

        song = disc.songs[0]
        assert song.song_id
        assert song.title
        assert song.album_id == "13788545"
        assert song.artists
        assert song.artists[0].artist_id

    def test_get_song_detail_returns_valid_response(self):
        with MelonClient() as client:
            chart = client.get_realtime_chart(page_size=1)
            top_song_id = chart.songs[0].song_id

            song_detail = client.get_song_detail(top_song_id)

        assert song_detail.result_code == "0"
        assert song_detail.song.song_id == top_song_id
        assert song_detail.song.title

    def test_get_artist_magazines_returns_valid_response(self):
        with MelonClient() as client:
            artist_magazines = client.get_artist_magazines("3709231")

        assert artist_magazines.result_code == "0"
        assert isinstance(artist_magazines.has_more, bool)
        assert len(artist_magazines.magazines) > 0

        first_magazine = artist_magazines.magazines[0]
        assert first_magazine.content_id
        assert first_magazine.content_name
        assert first_magazine.content_type_code
        assert first_magazine.content_img
        assert first_magazine.link
        assert first_magazine.artist_list