from pydantic import BaseModel, Field

class Artist(BaseModel):
    """A credited artist from a chart song's ``ARTISTLIST``."""
    artist_id: str = Field(alias="ARTISTID")
    name: str = Field(alias="ARTISTNAME")

class ArtistInfo(BaseModel):
    """Artist details embedded in a chart-report song, including optional profile data."""
    artist_id: str = Field(alias="ARTISTID")
    name: str = Field(alias="ARTISTNAME")
    act_type_name: str | None = Field(default=None, alias="ACTTYPENAME")
    debut_day: str | None = Field(default=None, alias="DEBUTDAY")
    birthday: str | None = Field(default=None, alias="BIRTHDAY")
    artist_img: str | None = Field(default=None, alias="ARTISTIMG")
    image_type: str | None = Field(default=None, alias="IMAGETYPE")
    content_type_code: str | None = Field(default=None, alias="CONTSTYPECODE")

class Genre(BaseModel):
    """A genre code and display name from a song's ``GENRELIST``."""
    genre_code: str = Field(alias="GENRECODE")
    genre_name: str = Field(alias="GENRENAME")

class ChartTLog(BaseModel):
    """Chart page metadata included in standard chart responses under ``TLOG``."""
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")

class ChartInfo(BaseModel):
    """The informational link supplied with Top 100, daily, weekly, and Hot 100."""
    link_url: str = Field(alias="LINKURL")
    link_type: str = Field(alias="LINKTYPE")

class TLog(BaseModel):
    """Expanded chart-report tracking metadata, including the reported song identity."""
    menu_id: str = Field(alias="MENUID")
    section: str = Field(alias="SECTION")
    page: str = Field(alias="PAGE")
    content_type_code: str = Field(alias="CONTSTYPECODE")
    content_type_name: str = Field(alias="CONTSTYPENAME")
    content_id: str = Field(alias="CONTSID")
    content_name: str = Field(alias="CONTSNAME")