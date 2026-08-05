from melon.base import BaseClient
from melon.models import ArtistSongs

ARTIST_SONGS_URL = "https://m2.melon.com/m6/v2/artist/music/songList.json"


class ArtistClient(BaseClient):
    def get_artist_songs(
        self,
        artist_id: str,
        caterogy_code: str = "",
        filter_by: str = "A",
        order_by: str = "NEW",
        page_size: int = 100,
        start_index: int = 1,
        cp_id: str = "IS40",
        cp_key: str = "17LNM9",
    ) -> ArtistSongs:
        """Fetch the song list for ``artist_id`` from the artist detail endpoint."""
        params = {
            "artistId": artist_id,
            "caterogyCode": caterogy_code,
            "filterBy": filter_by,
            "orderBy": order_by,
            "pageSize": page_size,
            "startIndex": start_index,
            "cpId": cp_id,
            "cpKey": cp_key,
        }
        response = self.client.get(ARTIST_SONGS_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return ArtistSongs.model_validate(raw["response"])