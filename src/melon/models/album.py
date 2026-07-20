from pydantic import BaseModel, Field

from .common import ArtistInfo, Genre, TLog

class Album(BaseModel):
    """Core album metadata returned in an album-detail response."""
    is_service: bool = Field(alias="ISSERVICE")
    album_id: str = Field(alias="ALBUMID")
    name: str = Field(alias="ALBUMNAME")
    issue_date: str = Field(alias="ISSUEDATE")
    is_track_zero: bool = Field(alias="ISTRACKZERO")
    album_img: str | None = Field(default=None, alias="ALBUMIMG")
    album_img_large: str | None = Field(default=None, alias="ALBUMIMGLARGE")
    song_cnt: int = Field(alias="SONGCNT")
    content_type: str = Field(alias="CTYPE")
    content_type_code: str = Field(alias="CONTSTYPECODE")
    artist_list: list[ArtistInfo] = Field(alias="ARTISTLIST")

class TotalAverageScoreInfo(BaseModel):
    """Rating availability copy and aggregate album rating."""
    title: str = Field(alias="TITLE")
    text: str = Field(alias="TEXT")
    score: float = Field(alias="TOTAVRGSCORE")
    participant_count: int = Field(alias="PTCPNMPRCO")

class TitleSongInfo(BaseModel):
    """The album's designated title song."""
    song_id: str = Field(alias="SONGID")
    title: str = Field(alias="SONGNAME")

class ArtistNoteInfo(BaseModel):
    """An artist note associated with an album release."""
    album_id: str = Field(alias="ALBUMID")
    artist_id: str = Field(alias="ARTISTID")
    note: str = Field(alias="ARTISTNOTE")
    artist_name: str = Field(alias="ARTISTNAME")
    artist_img: str | None = Field(default=None, alias="ARTISTIMG")
    issue_date: str = Field(alias="ISSUEDATE")

class MillionsLink(BaseModel):
    """Navigation target attached to an album's cumulative-listening milestone."""
    link_type: str = Field(alias="LINKTYPE")
    link_url: str = Field(alias="LINKURL")

class MillionsInfo(BaseModel):
    """Cumulative-listening milestone information for the album."""
    history_data: int = Field(alias="HISTDATA")
    issue_date: str = Field(alias="ISSUEDATE")
    history_info: str = Field(alias="HISTINFO")
    is_now: str = Field(alias="ISNOW")
    is_counting: str = Field(alias="ISCOUNTING")
    reaching_info: str = Field(alias="REACHINGINFO")
    accumulated_data: int = Field(alias="ACCUMDATA")
    link: MillionsLink = Field(alias="LINK")

class AlbumInfo(BaseModel):
    """Full album-detail response returned by Melon's album information endpoint."""
    result_code: str = Field(alias="RESULTCODE")
    response_type: str = Field(alias="RESPONSE")
    cp_plan_code: str = Field(alias="CPLANCODE")
    menu_id: str = Field(alias="MENUID")
    album: Album = Field(alias="ALBUMINFO")
    total_average_score_info: TotalAverageScoreInfo = Field(alias="TOTAVRGSCOREINFO")
    like_count: int = Field(alias="LIKECNT")
    is_dolby_atmos: bool = Field(alias="ISDOLBYATMOS")
    is_masterpiece: bool = Field(alias="ISMASTERPIECE")
    booklet_img_list: list | None = Field(alias="BOOKLETIMGLIST")
    album_price: str = Field(alias="ALBUMPRICE")
    album_price_flac16: str = Field(alias="ALBUMPRICEFLAC16")
    album_price_flac24: str = Field(alias="ALBUMPRICEFLAC24")
    album_flac_info: str = Field(alias="ALBUMFLACINFO")
    album_message: str = Field(alias="ALBUMMESSAGE")
    bbs_channel_seq: str = Field(alias="BBSCHANNELSEQ")
    bbs_contents_ref_value: str = Field(alias="BBSCONTSREFVALUE")
    post_img: str | None = Field(default=None, alias="POSTIMG")
    post_edit_img: str | None = Field(default=None, alias="POSTEDITIMG")
    title_song_info: TitleSongInfo | None = Field(default=None, alias="TITLESONGINFO")
    artist_note_info: ArtistNoteInfo | None = Field(default=None, alias="ARTISTNOTEINFO")
    artist_note_all_button_flag: bool = Field(alias="ARTISTNOTEALLBUTTONFLAG")
    genres: list[Genre] = Field(alias="GENRELIST")
    issue_date: str = Field(alias="ISSUEDATE")
    report: str = Field(alias="REPORT")
    album_type: str = Field(alias="ALBUMTYPE")
    seller_company: str = Field(alias="SELLCNPY")
    planning_company: str = Field(alias="PLANCNPY")
    credit_list: list | None = Field(alias="CREDITLIST")
    report_preview: str = Field(alias="REPORTPREVIEW")
    spotlight_button_flag: str = Field(alias="SPOTLIGHTBUTTONFLAG")
    hi_rising_button_flag: str = Field(alias="HIRISINGBUTTONFLAG")
    millions_info: MillionsInfo | None = Field(default=None, alias="MILLIONSINFO")
    dummy_text: str = Field(alias="DUMMYTEXT")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    tlog: TLog = Field(alias="TLOG")
