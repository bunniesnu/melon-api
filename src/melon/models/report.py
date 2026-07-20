from pydantic import BaseModel, Field

from .common import TLog
from .song import ReportSongInfo

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