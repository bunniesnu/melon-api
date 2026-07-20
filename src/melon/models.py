"""Pydantic models for the Melon chart JSON payloads used in the test fixtures.

Melon's API uses uppercase keys and represents many numeric values as strings.
Each field alias below maps one of those wire-format keys to a Pythonic attribute.
"""

from pydantic import BaseModel, Field, field_validator


# ---- Shared ----


class Artist(BaseModel):
    """A credited artist from a chart song's ``ARTISTLIST``."""
    artist_id: str = Field(alias="ARTISTID")
    name: str = Field(alias="ARTISTNAME")


# ---- Realtime Chart models ----


class Genre(BaseModel):
    """A genre code and display name from a song's ``GENRELIST``."""
    genre_code: str = Field(alias="GENRECODE")
    genre_name: str = Field(alias="GENRENAME")


class Song(BaseModel):
    """A chart song entry shared by realtime, Top 100, daily, weekly, and Hot 100.

    Fixture responses encode duration and ranks as strings; Pydantic coerces them
    to integers. Image URLs may be omitted, so the album-image variants are
    optional.
    """
    song_id: str = Field(alias="SONGID")
    title: str = Field(alias="SONGNAME")
    album_id: str = Field(alias="ALBUMID")
    album_name: str = Field(alias="ALBUMNAME")
    artists: list[Artist] = Field(alias="ARTISTLIST")
    play_time: int = Field(alias="PLAYTIME")
    genres: list[Genre] = Field(alias="GENRELIST")
    current_rank: int = Field(alias="CURRANK")
    past_rank: int = Field(alias="PASTRANK")
    rank_gap: int = Field(alias="RANKGAP")
    rank_type: str = Field(alias="RANKTYPE")
    is_mv: bool = Field(alias="ISMV")
    is_adult: bool = Field(alias="ISADULT")
    is_free: bool = Field(alias="ISFREE")
    is_hit_song: bool = Field(alias="ISHITSONG")
    is_holdback: bool = Field(alias="ISHOLDBACK")
    is_title_song: bool = Field(alias="ISTITLESONG")
    is_service: bool = Field(alias="ISSERVICE")
    is_track_zero: bool = Field(alias="ISTRACKZERO")
    album_img: str | None = Field(default=None, alias="ALBUMIMG")
    album_img_path: str | None = Field(default=None, alias="ALBUMIMGPATH")
    album_img_large: str | None = Field(default=None, alias="ALBUMIMGLARGE")
    album_img_small: str | None = Field(default=None, alias="ALBUMIMGSMALL")
    issue_date: str = Field(alias="ISSUEDATE")
    content_type: str = Field(alias="CTYPE")
    content_type_code: str = Field(alias="CONTSTYPECODE")

    @field_validator("current_rank", "past_rank", "rank_gap", "play_time", mode="before")
    @classmethod
    def empty_string_to_zero(cls, value):
        """Convert Melon's blank rank/duration value to the numeric sentinel ``0``."""
        if value == "":
            return 0
        return value

    @property
    def is_rising(self) -> bool:
        """Whether Melon reports an upward rank movement (``RANKTYPE == 'UP'``)."""
        return self.rank_type == "UP"


class ChartTLog(BaseModel):
    """Chart page metadata included in standard chart responses under ``TLOG``."""
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")


class ChartInfo(BaseModel):
    """The informational link supplied with Top 100, daily, weekly, and Hot 100."""
    link_url: str = Field(alias="LINKURL")
    link_type: str = Field(alias="LINKTYPE")


class RealtimeChart(BaseModel):
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


class Top100StatsElements(BaseModel):
    """Top 100 analytics identifiers returned in ``STATSELEMENTS``."""
    impression_id: str = Field(alias="IMPRESSIONID")
    range_code: str = Field(alias="RANGECODE")


class Top100Chart(BaseModel):
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


class DailyChart(BaseModel):
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


class WeeklyAwardEntry(BaseModel):
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


class MusicAward(BaseModel):
    """Weekly popularity-award metadata and its ranked vote entries."""
    title: str = Field(alias="TITLE")
    award_month: int = Field(alias="AWARDMONTH")
    award_week: int = Field(alias="AWARDWEEK")
    award_year: int = Field(alias="AWARDYEAR")
    award_day_of_month: int = Field(alias="AWARDDAYOFMONTH")
    subtitle: str = Field(alias="SUBTITLE")
    week_status: str = Field(alias="WEEKSTATUS")
    week_rank_list: list[WeeklyAwardEntry] = Field(alias="WEEKRANKLIST")


class WeeklyChart(BaseModel):
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


class Hot100Chart(BaseModel):
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


# ---- Chart Report models ----


class ReportArtist(BaseModel):
    """Artist details embedded in a chart-report song, including optional profile data."""
    artist_id: str = Field(alias="ARTISTID")
    name: str = Field(alias="ARTISTNAME")
    act_type_name: str | None = Field(default=None, alias="ACTTYPENAME")
    debut_day: str | None = Field(default=None, alias="DEBUTDAY")
    birthday: str | None = Field(default=None, alias="BIRTHDAY")
    artist_img: str | None = Field(default=None, alias="ARTISTIMG")
    image_type: str | None = Field(default=None, alias="IMAGETYPE")
    content_type_code: str | None = Field(default=None, alias="CONTSTYPECODE")


class ReportSongInfo(BaseModel):
    """Song metadata and current ranking at the top of a chart report."""
    song_id: str = Field(alias="SONGID")
    title: str = Field(alias="SONGNAME")
    album_id: str = Field(alias="ALBUMID")
    album_name: str = Field(alias="ALBUMNAME")
    artists: list[ReportArtist] = Field(alias="ARTISTLIST")
    issue_date: str = Field(alias="ISSUEDATE")
    album_img: str | None = Field(default=None, alias="ALBUMIMG")
    album_img_large: str | None = Field(default=None, alias="ALBUMIMGLARGE")
    album_img_small: str | None = Field(default=None, alias="ALBUMIMGSMALL")
    current_rank: int = Field(alias="CURRANK")
    past_rank: int = Field(alias="PASTRANK")
    rank_gap: int = Field(alias="RANKGAP")
    rank_type: str = Field(alias="RANKTYPE")

    @field_validator("current_rank", "past_rank", "rank_gap", mode="before")
    @classmethod
    def empty_string_to_zero(cls, value):
        """Convert a blank report rank from the API into ``0``."""
        if value == "":
            return 0
        return value


class ListenerChartTitle(BaseModel):
    """Templated listener-chart title; ``value`` replaces ``value_placeholder``."""
    value_placeholder: str = Field(alias="VALUEPLACEHOLDER")
    text: str = Field(alias="TEXT")
    value: str = Field(alias="VALUE")


class InfoListItem(BaseModel):
    """A title/text explanatory item shown with a chart report graph."""
    title: str = Field(alias="TITLE")
    text: str = Field(alias="TEXT")


class ListenerChartInfo(BaseModel):
    """Descriptive copy and update notes for the listener chart."""
    title: str = Field(alias="TITLE")
    desc: str = Field(alias="DESC")
    info_list: list[InfoListItem] = Field(alias="INFOLIST")
    foot: str | None = Field(default=None, alias="FOOT")


class ListenerChart(BaseModel):
    """Recent-listener graph, including axis bounds, observations, and display copy."""
    x_labels: list = Field(default_factory=list, alias="XLABELS")
    y_minimum: int = Field(alias="YMINIMUM")
    y_maximum: int = Field(alias="YMAXIMUM")
    data: list = Field(default_factory=list, alias="DATA")
    title: ListenerChartTitle = Field(alias="TITLE")
    info: ListenerChartInfo = Field(alias="INFO")


class ListenerData(BaseModel):
    """Current one-hour and one-day listener values; unavailable values are ``'-'``."""
    one_hour: str = Field(alias="ONEHOUR")
    one_day: str = Field(alias="ONEDAY")


class RankChartXLabel(BaseModel):
    """A rank-chart x-axis label, optionally highlighted for current/predicted time."""
    x_label: str = Field(alias="XLABEL")
    highlighting: bool = Field(alias="HIGHLIGHTING")


class RankChartDataPoint(BaseModel):
    """One actual or predicted rank observation in the chart report."""
    x_index: int = Field(alias="XINDEX")
    value: int = Field(alias="VALUE")
    label: str = Field(alias="LABEL")
    highlighting: bool = Field(alias="HIGHLIGHTING")


class RankChartTitle(BaseModel):
    """Templated title for the rank trend and prediction graph."""
    value_placeholder: str = Field(alias="VALUEPLACEHOLDER")
    text: str = Field(alias="TEXT")
    value: str = Field(alias="VALUE")


class RankChartInfo(BaseModel):
    """Descriptive copy and update notes for the rank trend graph."""
    title: str = Field(alias="TITLE")
    desc: str = Field(alias="DESC")
    info_list: list[InfoListItem] = Field(alias="INFOLIST")


class RankChart(BaseModel):
    """Rank history and optional predicted points from a song chart report."""
    x_labels: list[RankChartXLabel] = Field(alias="XLABELS")
    y_minimum: int = Field(alias="YMINIMUM")
    y_maximum: int = Field(alias="YMAXIMUM")
    data: list[RankChartDataPoint] = Field(alias="DATA")
    predicted_data: list[RankChartDataPoint] = Field(default_factory=list, alias="PREDICTEDDATA")
    title: RankChartTitle = Field(alias="TITLE")
    info: RankChartInfo = Field(alias="INFO")


class YesterChartInfoTitle(BaseModel):
    """Templated title describing the previous day's chart placement."""
    value_placeholder: str = Field(alias="VALUEPLACEHOLDER")
    text: str = Field(alias="TEXT")
    value: str = Field(alias="VALUE")


class YesterChartInfo(BaseModel):
    """Previous-day rank, best-record summaries, and daily-record metadata."""
    title: YesterChartInfoTitle = Field(alias="TITLE")
    first_info_label: str = Field(alias="FIRSTINFOLABEL")
    first_info_value: str = Field(alias="FIRSTINFOVALUE")
    second_info_label: str = Field(alias="SECONDINFOLABEL")
    second_info_value: str = Field(alias="SECONDINFOVALUE")
    record_list: list = Field(default_factory=list, alias="RECORDLIST")
    info: RankChartInfo = Field(alias="INFO")


class NextButton(BaseModel):
    """The next-song target exposed by the chart report footer."""
    song_id: str = Field(alias="SONGID")
    label: str = Field(alias="LABEL")


class FootButton(BaseModel):
    """Footer navigation container for a chart report."""
    next_button: NextButton = Field(alias="NEXTBUTTON")


class TLog(BaseModel):
    """Expanded chart-report tracking metadata, including the reported song identity."""
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    content_type_code: str = Field(alias="CONTSTYPECODE")
    content_type_name: str = Field(alias="CONTSTYPENAME")
    content_id: str = Field(alias="CONTSID")
    content_name: str = Field(alias="CONTSNAME")


class ChartReport(BaseModel):
    """Full per-song report: listener metrics, rank history, prediction, and daily record."""
    result_code: str = Field(alias="RESULTCODE")
    response_type: str = Field(alias="RESPONSE")
    cp_plan_code: str = Field(alias="CPLANCODE")
    recent_time: str = Field(alias="RECENTTIME")
    song_info: ReportSongInfo = Field(alias="SONGINFO")
    listener_chart: ListenerChart = Field(alias="LISTENERCHART")
    listener_data: ListenerData = Field(alias="LISTENERDATA")
    rank_chart: RankChart = Field(alias="RANKCHART")
    yester_chart_info: YesterChartInfo = Field(alias="YESTERCHARTINFO")
    foot_button: FootButton = Field(alias="FOOTBUTTON")
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: TLog = Field(alias="TLOG")


# ---- Chart Graph models ----


class GraphDataPoint(BaseModel):
    """An hourly Hot 100 graph point with score and rank-event flags."""
    x: int = Field(alias="X")
    value: float = Field(alias="VAL")
    top_count_tick: int = Field(alias="TOPCNTTIC")
    top_count_yn: str = Field(alias="TOPCNTYN")
    immediate_top_tick: bool = Field(alias="IMMTOPTIC")
    first_top_tick: bool = Field(alias="FSTTOPTIC")
    new_rank_tick: bool = Field(alias="NEWRANKTIC")


class EntGraphDataPoint(BaseModel):
    """An entertainment-chart rank point aligned to the hourly graph x-axis."""
    x: int = Field(alias="X")
    rank: int = Field(alias="RANK")


class GraphChartInfo(Song):
    """Song metadata embedded with an hourly graph series."""


class GraphDataList(BaseModel):
    """One song's hourly Hot 100 series and ranking summary."""
    graph_rank: int = Field(alias="GRAPHRANK")
    song_id: str = Field(alias="SONGID")
    peek_time: str = Field(alias="PEEKTIME")
    first_rank_serial_count: int = Field(alias="FIRSTRANKSERIALCOUNT")
    graph_data: list[GraphDataPoint] = Field(alias="GRAPHDATA")
    first_rank_count: int = Field(alias="FIRSTRANKCOUNT")
    ent_graph_data: list[EntGraphDataPoint] = Field(alias="ENTGRAPHDATA")
    graph_ent_chart: int = Field(alias="GRAPHENTCHART")
    graph_top7: int = Field(alias="GRAPHTOP7")
    graph_top_rank: int = Field(alias="GRAPHTOPRANK")
    graph_new_rank: str = Field(alias="GRAPHNEWRANK")
    graph_chart_info: GraphChartInfo = Field(alias="GRAPHCHARTINFO")
    share_value: int = Field(alias="SHAREVALUE")


class ChartGraph(BaseModel):
    """Hourly Hot 100 graph response with shared categories and per-song series."""
    x_categories: list[str] = Field(alias="XCATE")
    ent_chart_x_categories: list[str] = Field(alias="ENTCHARTXCATE")
    standard: str = Field(alias="STANDARD")
    graph_data_list: list[GraphDataList] = Field(alias="GRAPHDATALIST")
    five_chart_flag: str = Field(alias="FIVECHARTFLAG")
    rank_day: str = Field(alias="RANKDAY")
    rank_hour: str = Field(alias="RANKHOUR")
    all_rank: str = Field(alias="ALLRANK")
    comp_rank: str = Field(alias="COMPRANK")
    chart_info: ChartInfo = Field(alias="CHARTINFO")
    status: str = Field(alias="STATUS")
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: ChartTLog = Field(alias="TLOG")


# ---- Hot100 Chart Graph models ----


class FiveGraphDataPoint(BaseModel):
    """A five-minute Hot 100 graph score point."""
    x: int = Field(alias="X")
    value: float = Field(alias="VAL")


class FiveGraphDataList(BaseModel):
    """One song's five-minute graph series and current score summary."""
    song_id: str = Field(alias="SONGID")
    last_group_current_score: float = Field(alias="LSTGRPCURSCORE")
    graph_data: list[FiveGraphDataPoint] = Field(alias="GRAPHDATA")
    graph_chart_info: GraphChartInfo = Field(alias="GRAPHCHARTINFO")
    graph_rank: int = Field(alias="GRAPHRANK")
    share_value: int = Field(alias="SHAREVALUE")


class FiveGraph(BaseModel):
    """Five-minute Hot 100 graph response returned by the graph endpoint."""
    graph_data_list: list[FiveGraphDataList] = Field(alias="GRAPHDATALIST")
    x_categories: list[str] = Field(alias="XCATE")
    five_time: str = Field(alias="FIVETIME")
    rank_day: str = Field(alias="RANKDAY")
    rank_hour: str = Field(alias="RANKHOUR")
    five_error_flag: bool = Field(alias="FIVEERRORFLAG")
    status: str = Field(alias="STATUS")
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: ChartTLog = Field(alias="TLOG")


# ---- Artist Chart models ----


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
