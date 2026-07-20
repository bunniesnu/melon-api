from pydantic import BaseModel

class MelonModel(BaseModel):
    @staticmethod
    def blank_to_zero(value):
        """Convert a blank value into ``0``."""
        return 0 if value == "" else value