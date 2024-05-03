from pydantic import BaseModel

class Mode(BaseModel):
    place: str
    program: str
    data: str | None | dict