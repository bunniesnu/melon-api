from pydantic import Field

from .base import MelonModel
from .common import ChartInfo, ChartTLog
from .song import Song

class Top100StatsElements(MelonModel):
    """Top 100 analytics identifiers returned in ``STATSELEMENTS``."""
    impression_id: str = Field(alias="IMPRESSIONID")
    range_code: str = Field(alias="RANGECODE")

class RealtimeChart(MelonModel):
    """Hourly chart response: ``CHARTLIST`` songs and the ``RANKDAY``/``RANKHOUR`` snapshot."""
    status: str = Field(alias="STATUS")
    recommend_list: list = Field(default_factory=list, alias="RECOMMENDLIST")
    songs: list[Song] = Field(alias="CHARTLIST")
    rank_day: str = Field(alias="RANKDAY")
    rank_hour: str = Field(alias="RANKHOUR")
    has_more: bool = Field(alias="HASMORE")
    size: int = Field(alias="SIZE")
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: ChartTLog = Field(alias="TLOG")

class Top100Chart(MelonModel):
    """Current Top 100 response, whose songs are returned as ``SONGLIST``."""
    rank_day: str = Field(alias="RANKDAY")
    rank_hour: str = Field(alias="RANKHOUR")
    status: str = Field(alias="STATUS")
    songs: list[Song] = Field(alias="SONGLIST")
    chart_info: ChartInfo = Field(alias="CHARTINFO")
    stats_elements: Top100StatsElements = Field(alias="STATSELEMENTS")
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: ChartTLog = Field(alias="TLOG")

class DailyChart(MelonModel):
    """Daily Top 100 response; ``RANKDAY`` can be null in the fixture payload."""
    status: str = Field(alias="STATUS")
    recommend_list: list = Field(default_factory=list, alias="RECOMMENDLIST")
    songs: list[Song] = Field(alias="CHARTLIST")
    chart_info: ChartInfo = Field(alias="CHARTINFO")
    rank_day: str | None = Field(alias="RANKDAY")
    has_more: bool = Field(alias="HASMORE")
    size: int = Field(alias="SIZE")
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: ChartTLog = Field(alias="TLOG")

class WeeklyAwardEntry(MelonModel):
    """One ranked candidate in the weekly popularity award's ``WEEKRANKLIST``."""
    current_rank: int = Field(alias="CURRANK")
    song_name: str = Field(alias="SONGNAME")
    artist_id: str = Field(alias="ARTISTID")
    artist_name: str = Field(alias="ARTISTNAME")
    artist_img: str | None = Field(default=None, alias="ARTISTIMG")
    artist_img_large: str | None = Field(default=None, alias="ARTISTIMGLARGE")
    artist_img_small: str | None = Field(default=None, alias="ARTISTIMGSMALL")
    vote_percent: int = Field(alias="VOTEPER")
    start_month: int = Field(alias="STARTMONTH")
    start_week: int = Field(alias="STARTWEEK")

class MusicAward(MelonModel):
    """Weekly popularity-award metadata and its ranked vote entries."""
    title: str = Field(alias="TITLE")
    award_month: int = Field(alias="AWARDMONTH")
    award_week: int = Field(alias="AWARDWEEK")
    award_year: int = Field(alias="AWARDYEAR")
    award_day_of_month: int = Field(alias="AWARDDAYOFMONTH")
    subtitle: str = Field(alias="SUBTITLE")
    week_status: str = Field(alias="WEEKSTATUS")
    week_rank_list: list[WeeklyAwardEntry] = Field(alias="WEEKRANKLIST")

class WeeklyChart(MelonModel):
    """Weekly Top 100 response, including its chart date range and music award."""
    music_award: MusicAward = Field(alias="MUSICAWARD")
    status: str = Field(alias="STATUS")
    review: dict | None = Field(default=None, alias="REVIEW")
    recommend_list: list = Field(default_factory=list, alias="RECOMMENDLIST")
    songs: list[Song] = Field(alias="CHARTLIST")
    start_day: str = Field(alias="STARTDAY")
    end_day: str = Field(alias="ENDDAY")
    has_more: bool = Field(alias="HASMORE")
    size: int = Field(alias="SIZE")
    chart_info: ChartInfo = Field(alias="CHARTINFO")
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: ChartTLog = Field(alias="TLOG")

class Hot100Chart(MelonModel):
    """Hot 100 chart snapshot, with songs returned under ``SONGLIST``."""
    rank_day: str = Field(alias="RANKDAY")
    rank_hour: str = Field(alias="RANKHOUR")
    status: str = Field(alias="STATUS")
    songs: list[Song] = Field(alias="SONGLIST")
    chart_info: ChartInfo = Field(alias="CHARTINFO")
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: ChartTLog = Field(alias="TLOG")