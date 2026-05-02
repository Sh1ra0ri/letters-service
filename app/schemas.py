from pydantic import BaseModel


class Letter(BaseModel):
    name: str
    message: str
    contacts: str
