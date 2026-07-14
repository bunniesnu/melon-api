from pydantic import BaseModel, Field, field_validator


class Artist(BaseModel):
    artist_id: str = Field(alias="ARTISTID")
    name: str = Field(alias="ARTISTNAME")


class ChartSong(BaseModel):
    song_id: str = Field(alias="SONGID")
    title: str = Field(alias="SONGNAME")
    album_name: str = Field(alias="ALBUMNAME")
    artists: list[Artist] = Field(alias="ARTISTLIST")
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

    @property
    def is_rising(self) -> bool:
        return self.rank_type == "UP"


class SongInfo(BaseModel):
    song_id: str = Field(alias="SONGID")
    title: str = Field(alias="SONGNAME")
    album_name: str = Field(alias="ALBUMNAME")
    current_rank: int = Field(alias="CURRANK")
    past_rank: int = Field(alias="PASTRANK")


class ChartReport(BaseModel):
    song_info: SongInfo = Field(alias="SONGINFO")
