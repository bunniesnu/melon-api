from pydantic import Field

from melon.models.base import MelonModel
from melon.models.common import ChartInfo

class MagazineArtist(MelonModel):
    """An artist associated with a magazine entry."""
    artist_id: str = Field(alias="ARTISTID")
    name: str = Field(alias="ARTISTNAME")

class Magazine(MelonModel):
    """A magazine entry returned by the Melon magazine endpoint."""
    content_type_code: str = Field(alias="CONTSTYPECODE")
    content_id: str = Field(alias="CONTSID")
    content_name: str = Field(alias="CONTSNAME")
    artist_list: list[MagazineArtist] = Field(alias="ARTISTLIST")
    content_img: str = Field(alias="CONTSIMG")
    link: ChartInfo = Field(alias="LINK")