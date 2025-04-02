from pydantic import BaseModel


class body(BaseModel):
    username: str
    room : str
    text : str