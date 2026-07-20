"""Pydantic models for the Melon chart JSON payloads used in the test fixtures.

Melon's API uses uppercase keys and represents many numeric values as strings.
Each field alias below maps one of those wire-format keys to a Pythonic attribute.
"""

from .album import (
    AlbumInfo
)
from .artist import (
    ArtistChart
)
from .charts import (
    DailyChart,
    Hot100Chart,
    RealtimeChart,
    Top100Chart,
    WeeklyChart,
)
from .report import (
    ChartReport
)
from .graph import (
    ChartGraph,
    FiveGraph
)
from .song import (
    Song
)
from .common import (
    Artist,
    Genre
)

__all__ = [
    "Artist",
    "Genre",
    "Song",
    "RealtimeChart",
    "Top100Chart",
    "DailyChart",
    "WeeklyChart",
    "Hot100Chart",
    "ChartReport",
    "ChartGraph",
    "FiveGraph",
    "ArtistChart",
    "AlbumInfo",
]