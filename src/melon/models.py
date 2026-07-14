from pydantic import BaseModel, Field, field_validator


# ---- Shared ----


class Artist(BaseModel):
    artist_id: str = Field(alias="ARTISTID")
    name: str = Field(alias="ARTISTNAME")


# ---- Hourly Chart models ----


class Genre(BaseModel):
    genre_code: str = Field(alias="GENRECODE")
    genre_name: str = Field(alias="GENRENAME")


class ChartSong(BaseModel):
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
        if value == "":
            return 0
        return value

    @property
    def is_rising(self) -> bool:
        return self.rank_type == "UP"


class ChartTLog(BaseModel):
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")


class HourlyChart(BaseModel):
    status: str = Field(alias="STATUS")
    recommend_list: list = Field(default_factory=list, alias="RECOMMENDLIST")
    songs: list[ChartSong] = Field(alias="CHARTLIST")
    rank_day: str = Field(alias="RANKDAY")
    rank_hour: str = Field(alias="RANKHOUR")
    has_more: bool = Field(alias="HASMORE")
    size: int = Field(alias="SIZE")
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: ChartTLog = Field(alias="TLOG")


# ---- Chart Report models ----


class ReportArtist(BaseModel):
    artist_id: str = Field(alias="ARTISTID")
    name: str = Field(alias="ARTISTNAME")
    act_type_name: str | None = Field(default=None, alias="ACTTYPENAME")
    debut_day: str | None = Field(default=None, alias="DEBUTDAY")
    birthday: str | None = Field(default=None, alias="BIRTHDAY")
    artist_img: str | None = Field(default=None, alias="ARTISTIMG")
    image_type: str | None = Field(default=None, alias="IMAGETYPE")
    content_type_code: str | None = Field(default=None, alias="CONTSTYPECODE")


class ReportSongInfo(BaseModel):
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
        if value == "":
            return 0
        return value


class ListenerChartTitle(BaseModel):
    value_placeholder: str = Field(alias="VALUEPLACEHOLDER")
    text: str = Field(alias="TEXT")
    value: str = Field(alias="VALUE")


class InfoListItem(BaseModel):
    title: str = Field(alias="TITLE")
    text: str = Field(alias="TEXT")


class ListenerChartInfo(BaseModel):
    title: str = Field(alias="TITLE")
    desc: str = Field(alias="DESC")
    info_list: list[InfoListItem] = Field(alias="INFOLIST")
    foot: str | None = Field(default=None, alias="FOOT")


class ListenerChart(BaseModel):
    x_labels: list = Field(default_factory=list, alias="XLABELS")
    y_minimum: int = Field(alias="YMINIMUM")
    y_maximum: int = Field(alias="YMAXIMUM")
    data: list = Field(default_factory=list, alias="DATA")
    title: ListenerChartTitle = Field(alias="TITLE")
    info: ListenerChartInfo = Field(alias="INFO")


class ListenerData(BaseModel):
    one_hour: str = Field(alias="ONEHOUR")
    one_day: str = Field(alias="ONEDAY")


class RankChartXLabel(BaseModel):
    x_label: str = Field(alias="XLABEL")
    highlighting: bool = Field(alias="HIGHLIGHTING")


class RankChartDataPoint(BaseModel):
    x_index: int = Field(alias="XINDEX")
    value: int = Field(alias="VALUE")
    label: str = Field(alias="LABEL")
    highlighting: bool = Field(alias="HIGHLIGHTING")


class RankChartTitle(BaseModel):
    value_placeholder: str = Field(alias="VALUEPLACEHOLDER")
    text: str = Field(alias="TEXT")
    value: str = Field(alias="VALUE")


class RankChartInfo(BaseModel):
    title: str = Field(alias="TITLE")
    desc: str = Field(alias="DESC")
    info_list: list[InfoListItem] = Field(alias="INFOLIST")


class RankChart(BaseModel):
    x_labels: list[RankChartXLabel] = Field(alias="XLABELS")
    y_minimum: int = Field(alias="YMINIMUM")
    y_maximum: int = Field(alias="YMAXIMUM")
    data: list[RankChartDataPoint] = Field(alias="DATA")
    predicted_data: list[RankChartDataPoint] = Field(default_factory=list, alias="PREDICTEDDATA")
    title: RankChartTitle = Field(alias="TITLE")
    info: RankChartInfo = Field(alias="INFO")


class YesterChartInfoTitle(BaseModel):
    value_placeholder: str = Field(alias="VALUEPLACEHOLDER")
    text: str = Field(alias="TEXT")
    value: str = Field(alias="VALUE")


class YesterChartInfo(BaseModel):
    title: YesterChartInfoTitle = Field(alias="TITLE")
    first_info_label: str = Field(alias="FIRSTINFOLABEL")
    first_info_value: str = Field(alias="FIRSTINFOVALUE")
    second_info_label: str = Field(alias="SECONDINFOLABEL")
    second_info_value: str = Field(alias="SECONDINFOVALUE")
    record_list: list = Field(default_factory=list, alias="RECORDLIST")
    info: RankChartInfo = Field(alias="INFO")


class NextButton(BaseModel):
    song_id: str = Field(alias="SONGID")
    label: str = Field(alias="LABEL")


class FootButton(BaseModel):
    next_button: NextButton = Field(alias="NEXTBUTTON")


class TLog(BaseModel):
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    content_type_code: str = Field(alias="CONTSTYPECODE")
    content_type_name: str = Field(alias="CONTSTYPENAME")
    content_id: str = Field(alias="CONTSID")
    content_name: str = Field(alias="CONTSNAME")


class ChartReport(BaseModel):
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
