from pydantic import BaseModel, Field

from .common import ChartInfo, ChartTLog
from .song import GraphChartInfo

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