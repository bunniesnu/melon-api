from pydantic import Field, field_validator

from melon.models.base import MelonModel
from melon.models.common import Artist, ArtistInfo, Genre, TLog

class BaseSong(MelonModel):
    """Base song metadata shared by chart and report responses."""
    song_id: str = Field(alias="SONGID")
    title: str = Field(alias="SONGNAME")
    album_id: str = Field(alias="ALBUMID")
    album_name: str = Field(alias="ALBUMNAME")
    artists: list[Artist] = Field(alias="ARTISTLIST")
    play_time: int = Field(alias="PLAYTIME")
    genres: list[Genre] = Field(alias="GENRELIST")
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

    @field_validator("play_time", mode="before")
    @classmethod
    def empty_string_to_zero(cls, value):
        return cls.blank_to_zero(value)

class ChartSong(BaseSong):
    """A chart song entry shared by realtime, Top 100, daily, weekly, and Hot 100.

    Fixture responses encode duration and ranks as strings; Pydantic coerces them
    to integers. Image URLs may be omitted, so the album-image variants are
    optional.
    """
    current_rank: int = Field(alias="CURRANK")
    past_rank: int = Field(alias="PASTRANK")
    rank_gap: int = Field(alias="RANKGAP")
    rank_type: str = Field(alias="RANKTYPE")

    @field_validator("current_rank", "past_rank", "rank_gap", mode="before")
    @classmethod
    def empty_string_to_zero(cls, value):
        return cls.blank_to_zero(value)

    @property
    def is_rising(self) -> bool:
        """Whether Melon reports an upward rank movement (``RANKTYPE == 'UP'``)."""
        return self.rank_type == "UP"

class ReportSongInfo(MelonModel):
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
        return cls.blank_to_zero(value)

class GraphChartInfo(ChartSong):
    """Song metadata embedded with an hourly graph series."""

class FiveGraphChartInfo(BaseSong):
    """Song metadata embedded with a five-minute interval graph series."""

class AlbumSong(BaseSong):
    track_no: int = Field(alias="TRACKNO")


class SongDetailSong(BaseSong):
    """Song metadata at the top of a song-detail response."""
    is_flac_available: bool = Field(alias="ISFLACAVAIL")
    is_flac16_available: bool = Field(alias="ISFLAC16AVAIL")
    is_flac24_available: bool = Field(alias="ISFLAC24AVAIL")


class SongDetailAlbum(MelonModel):
    """Album metadata embedded in a song-detail response."""
    is_service: bool = Field(alias="ISSERVICE")
    album_id: str = Field(alias="ALBUMID")
    name: str = Field(alias="ALBUMNAME")
    artists: list[Artist] = Field(alias="ARTISTLIST")
    issue_date: str = Field(alias="ISSUEDATE")
    is_track_zero: bool = Field(alias="ISTRACKZERO")
    album_img: str | None = Field(default=None, alias="ALBUMIMG")
    album_img_large: str | None = Field(default=None, alias="ALBUMIMGLARGE")
    like_count: int = Field(alias="LIKECNT")
    song_count: int = Field(alias="SONGCNT")
    content_type: str = Field(alias="CTYPE")
    content_type_code: str = Field(alias="CONTSTYPECODE")


class SongStyle(MelonModel):
    """A style tag attached to a song-detail response."""
    style_code: str = Field(alias="STYLECODE")
    name: str = Field(alias="STYLENAME")


class GenderPercent(MelonModel):
    """Listener gender percentages in the streaming report."""
    male: int = Field(alias="MALE")
    female: int = Field(alias="FEMALE")


class StreamReportInfo(MelonModel):
    """Listening statistics displayed on a song's detail page."""
    daily_listener_count: int | None = Field(alias="DAILYLISTENERCNT")
    total_listen_count: int | None = Field(alias="TOTALLISTENCNT")
    total_listener_count: int | None = Field(alias="TOTALLISTENERCNT")
    gender_percent: GenderPercent | None = Field(alias="GENDERPERCENT")
    age_percent: list[int] = Field(alias="AGEPERCENT")
    guide: str = Field(alias="GUIDE")

    @field_validator("gender_percent", mode="before")
    @classmethod
    def empty_gender_percent_to_none(cls, value):
        if value == {}:
            return None
        return value

    @field_validator("daily_listener_count", "total_listen_count", "total_listener_count", mode="before")
    @classmethod
    def validate_counts(cls, value):
        if value == "":
            return None
        if isinstance(value, str):
            return int(value.replace(",", ""))
        return value


class SongAchievementInfo(MelonModel):
    """Chart-achievement data displayed on a song's detail page."""
    best_rank: int = Field(alias="BESTRANK")
    best_rank_date: str = Field(alias="BESTRANKDATE")
    yesterday_chart_rank: int = Field(alias="YESTERDAYCHARTRANK")
    is_in_chart: bool = Field(alias="INCHARTYN")
    has_chart_history: bool = Field(alias="HASCHARTINHISTORY")
    guide: str = Field(alias="GUIDE")


class SongDetail(MelonModel):
    """Full response payload returned by Melon's song-detail endpoint.

    Validate the endpoint's unwrapped ``response`` object with this model.
    """
    result_code: str = Field(alias="RESULTCODE")
    response_type: str = Field(alias="RESPONSE")
    cp_plan_code: str = Field(alias="CPLANCODE")
    menu_id: str = Field(alias="MENUID")
    song: SongDetailSong = Field(alias="SONGINFO")
    artists: list[ArtistInfo] = Field(alias="ARTISTLIST")
    song_flac_info: str = Field(alias="SONGFLACINFO")
    is_dolby_atmos: bool = Field(alias="ISDOLBYATMOS")
    album: SongDetailAlbum = Field(alias="ALBUMINFO")
    booklet_img_list: list | None = Field(alias="BOOKLETIMGLIST")
    like_count: int = Field(alias="LIKECNT")
    lyrics: str = Field(alias="LYRIC")
    is_highlight_available: bool = Field(alias="ISHIGHLIGHTAVAIL")
    lyric_tooltip_message: str = Field(alias="LYRICTOOLTIPMSG")
    styles: list[SongStyle] | None = Field(alias="STYLELIST")
    genres: list[Genre] = Field(alias="GENRELIST")
    lyricists: list[ArtistInfo] = Field(alias="LYSTLIST")
    composers: list[ArtistInfo] = Field(alias="CMPSRLIST")
    arrangers: list[ArtistInfo] = Field(alias="ARNGRLIST")
    bbs_channel_seq: str = Field(alias="BBSCHANNELSEQ")
    bbs_contents_ref_value: str = Field(alias="BBSCONTSREFVALUE")
    post_img: str | None = Field(default=None, alias="POSTIMG")
    post_edit_img: str | None = Field(default=None, alias="POSTEDITIMG")
    stream_report: StreamReportInfo = Field(alias="STREAMREPORTINFO")
    achievement: SongAchievementInfo | None = Field(alias="SONGACHIEVEMENTINFO")
    dummy_text: str = Field(alias="DUMMYTEXT")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: TLog = Field(alias="TLOG")
