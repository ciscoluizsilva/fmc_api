from pydantic import BaseModel

class Domain(BaseModel):
    uuid: str
    name: str
    type: str