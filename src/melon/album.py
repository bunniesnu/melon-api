from melon.base import BaseClient
from melon.models import AlbumInfo

ALBUM_INFO_URL = "https://m2.melon.com/m6/v3/album/info.json"

class AlbumClient(BaseClient):
    def get_album_info(
        self,
        album_id: str,
        cp_id: str = "AS40",
        cp_key: str = "14LNC3",
        app_ver: str = "6.2.0",
    ) -> AlbumInfo:
        """Fetch metadata, credits, ratings, and notes for ``album_id``."""
        params = {
            "albumId": album_id,
            "cpId": cp_id,
            "cpKey": cp_key,
            "appVer": app_ver,
        }
        response = self.client.get(ALBUM_INFO_URL, params=params)
        response.raise_for_status()
        raw = response.json()
        return AlbumInfo.model_validate(raw["response"])