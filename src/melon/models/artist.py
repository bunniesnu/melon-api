from pydantic import Field, field_validator

from melon.models.base import MelonModel
from melon.models.common import Artist, ChartTLog, TLog
from melon.models.song import BaseSong

class SearchTypeItem(MelonModel):
    """An artist-chart category option from ``SEARCHTYPELIST``."""
    type_code: str = Field(alias="TYPECODE")
    type_code_name: str = Field(alias="TYPECODENAME")

class ArtistChartInfo(MelonModel):
    """Link metadata that accompanies the artist chart."""
    open_link: str = Field(alias="OPENLINK")
    open_type: str = Field(alias="OPENTYPE")

class ArtistChartEntry(MelonModel):
    """One artist-chart ranking with fan counts and the component score indices."""
    artist_id: str = Field(alias="ARTISTID")
    name: str = Field(alias="ARTISTNAME")
    act_type_name: str = Field(alias="ACTTYPENAME")
    debut_day: str | None = Field(default=None, alias="DEBUTDAY")
    birthday: str | None = Field(default=None, alias="BIRTHDAY")
    artist_img: str | None = Field(default=None, alias="ARTISTIMG")
    current_rank: int = Field(alias="CURRANK")
    past_rank: int = Field(alias="PASTRANK")
    rank_gap: int = Field(alias="RANKGAP")
    rank_type: str = Field(alias="RANKTYPE")
    area_type: str = Field(alias="AREATYPE")
    total_fan_count: int = Field(alias="TOTFANCNT")
    increment_fan_count: int = Field(alias="INCREMFANCNT")
    increment_type: str = Field(alias="INCREMTYPE")
    song_index: float = Field(alias="SONGIDX")
    mv_index: float = Field(alias="MVIDX")
    photo_index: float = Field(alias="PHOTOIDX")
    fan_index: float = Field(alias="FANIDX")
    like_index: float = Field(alias="LIKEIDX")
    toc_index: float = Field(alias="TOCIDX")
    channel_seq: str = Field(alias="CHNLSEQ")
    top_rank: int = Field(alias="TOPRANK")
    past_week_rank: int = Field(alias="PASTWEEKRANK")
    image_type: str = Field(alias="IMAGETYPE")
    content_type_code: str = Field(alias="CONTSTYPECODE")

    @field_validator("current_rank", "past_rank", "rank_gap", mode="before")
    @classmethod
    def empty_string_to_zero(cls, value):
        return cls.blank_to_zero(value)

class ArtistChart(MelonModel):
    """Artist chart response, including category choices and ranked artist entries."""
    status: str = Field(alias="STATUS")
    search_type_list: list[SearchTypeItem] = Field(alias="SEARCHTYPELIST")
    artists: list[ArtistChartEntry] = Field(alias="CHARTLIST")
    rank_day: str = Field(alias="RANKDAY")
    has_more: bool = Field(alias="HASMORE")
    size: int = Field(alias="SIZE")
    chart_info: ArtistChartInfo = Field(alias="CHARTINFO")
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: ChartTLog = Field(alias="TLOG")

class ArtistSong(BaseSong):
     """A song listed on an artist's song-list endpoint."""

class ArtistSongs(MelonModel):
    """Artist song-list response, including pagination state and tracked songs."""

    result_code: str = Field(alias="RESULTCODE")
    menu_id: str = Field(alias="MENUID")
    has_more: bool = Field(alias="HASMORE")
    songs: list[ArtistSong] = Field(alias="SONGLIST")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: TLog = Field(alias="TLOG")


class ArtistAlbum(MelonModel):
    """An album listed on an artist's album-list endpoint."""

    is_service: bool = Field(alias="ISSERVICE")
    album_id: str = Field(alias="ALBUMID")
    album_name: str = Field(alias="ALBUMNAME")
    artist_list: list[Artist] = Field(alias="ARTISTLIST")
    issue_date: str = Field(alias="ISSUEDATE")
    is_track_zero: bool = Field(alias="ISTRACKZERO")
    album_img: str = Field(alias="ALBUMIMG")
    album_img_large: str = Field(alias="ALBUMIMGLARGE")
    song_cnt: int = Field(alias="SONGCNT")
    content_type: str = Field(alias="CTYPE")
    content_type_code: str = Field(alias="CONTSTYPECODE")
    is_masterpiece: bool = Field(alias="ISMASTERPIECE")


class ArtistAlbums(MelonModel):
    """Artist album-list response, including pagination state and album entries."""

    result_code: str = Field(alias="RESULTCODE")
    menu_id: str = Field(alias="MENUID")
    has_more: bool = Field(alias="HASMORE")
    albums: list[ArtistAlbum] = Field(alias="ALBUMLIST")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: TLog = Field(alias="TLOG")