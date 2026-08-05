from melon.base import BaseClient
from melon.models import SongDetail

SONG_DETAIL_URL = "https://m2.melon.com/m6/v5/song/info.json"

class SongClient(BaseClient):
    def get_song_detail(
        self,
        song_id: str,
        adult_flag: int = 3,
        cp_id: str = "IS40",
        cp_key: str = "17LNM9",
    ) -> SongDetail:
        """Fetch the song-detail response for ``song_id``."""
        params = {
            "cpId": cp_id,
            "cpKey": cp_key,
            "adultFlg": adult_flag,
            "songId": song_id,
        }
        response = self.client.get(SONG_DETAIL_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return SongDetail.model_validate(raw["response"])