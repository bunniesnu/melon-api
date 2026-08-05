from pydantic import Field

from melon.models.base import MelonModel


class Photo(MelonModel):
    """A photo listed on an artist's photo-list endpoint."""

    photo_id: str = Field(alias="PHOTOID")
    photo_img: str = Field(alias="PHOTOIMG")
    photo_name: str = Field(alias="PHOTONAME")