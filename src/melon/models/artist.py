from pydantic import BaseModel, Field, field_validator

from .common import ChartTLog

class SearchTypeItem(BaseModel):
    """An artist-chart category option from ``SEARCHTYPELIST``."""
    type_code: str = Field(alias="TYPECODE")
    type_code_name: str = Field(alias="TYPECODENAME")

class ArtistChartInfo(BaseModel):
    """Link metadata that accompanies the artist chart."""
    open_link: str = Field(alias="OPENLINK")
    open_type: str = Field(alias="OPENTYPE")

class ArtistChartEntry(BaseModel):
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
        """Convert a blank artist-chart rank from the API into ``0``."""
        if value == "":
            return 0
        return value

class ArtistChart(BaseModel):
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