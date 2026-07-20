from pydantic import BaseModel, Field, field_validator

from .common import Artist, ArtistInfo, Genre

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

class ReportSongInfo(BaseModel):
    """Song metadata and current ranking at the top of a chart report."""
    song_id: str = Field(alias="SONGID")
    title: str = Field(alias="SONGNAME")
    album_id: str = Field(alias="ALBUMID")
    album_name: str = Field(alias="ALBUMNAME")
    artists: list[ArtistInfo] = Field(alias="ARTISTLIST")
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

class GraphChartInfo(Song):
    """Song metadata embedded with an hourly graph series."""