from pydantic import BaseModel
from typing import Optional

class Links(BaseModel):
    self: str
    parent: Optional[str] = None

class Parent(BaseModel):
    id: str
    type: str


class Target(BaseModel):
    name: str
    id: str
    type: str


class Overrides(BaseModel):
    parent: Parent
    target: Target


class LastUser(BaseModel):
    name: str


class Domain(BaseModel):
    name: str
    id: str


class Metadata(BaseModel):
    lastUser: LastUser
    domain: Optional[Domain] = None
    ipType: Optional[str] = None
    parentType: str

class Literal(BaseModel):
    type: str
    value: str