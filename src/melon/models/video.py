from pydantic import Field

from melon.models.base import MelonModel
from melon.models.common import Artist


class VideoRepartList(MelonModel):
    """The highlighted artist block embedded in an artist video entry."""

    artist_id: str = Field(alias="ARTISTID")
    name: str = Field(alias="ARTISTNAME")
    artist_img: str | None = Field(default=None, alias="ARTISTIMG")
    is_brand_js: bool = Field(alias="ISBRANDJS")


class Video(MelonModel):
    """A video listed on an artist's video-list endpoint."""

    mv_id: str = Field(alias="MVID")
    name: str = Field(alias="MVNAME")
    brand_key: str = Field(alias="BRANDKEY")
    repartist: VideoRepartList = Field(alias="REPARTIST")
    artists: list[Artist] = Field(alias="ARTISTLIST")
    adult_grade: str = Field(alias="ADULTGRADE")
    song_id: str = Field(alias="SONGID")
    song_name: str = Field(alias="SONGNAME")
    play_time: int = Field(alias="PLAYTIME")
    is_song: bool = Field(alias="ISSONG")
    is_adult: bool = Field(alias="ISADULT")
    is_service: bool = Field(alias="ISSERVICE")
    issue_date: str = Field(alias="ISSUEDATE")
    mv_img: str = Field(alias="MVIMG")
    mv169_img: str = Field(alias="MV169IMG")
    is_mv: bool = Field(alias="ISMV")
    is_live: bool = Field(alias="ISLIVE")
    is_livestreaming: bool = Field(alias="ISLIVESTREAMING")
    view_count: int = Field(alias="VIEWCNT")
    mv_desc: str = Field(alias="MVDESC")
    album_id: str | None = Field(default=None, alias="ALBUMID")
    album_name: str | None = Field(default=None, alias="ALBUMNAME")
    prog_seq: str = Field(alias="PROGSEQ")
    prog_name: str = Field(alias="PROGNAME")
    epsd_name: str = Field(alias="EPSDNAME")
    epsd_no: str = Field(alias="EPSDNO")
    epsd_no_name: str = Field(alias="EPSDNONAME")
    content_type: str = Field(alias="CTYPE")
    content_type_code: str = Field(alias="CONTSTYPECODE")