from .general import Links, Overrides, Metadata, Literal
from pydantic import BaseModel
from typing import Optional, List

class NetworkObject(BaseModel):
    links: Optional[Links] = None
    type: str
    value: Optional[str] = None
    overrides: Optional[Overrides] = None
    overridable: Optional[bool] = None
    description: Optional[str] = None
    name: str
    id: Optional[str] = None
    metadata: Optional[Metadata] = None 

class HostObject(BaseModel):
    links: Optional[Links] = None
    type: str
    value: Optional[str] = None
    overridable: Optional[bool] = None
    description: Optional[str] = None
    id: Optional[str] = None
    name: str
    metadata: Optional[Metadata] = None

class NetworkGroups(BaseModel):
    metadata: Optional[Metadata] = None
    literals: Optional[List[Literal]] = None
    overridable: Optional[bool] = None
    name: str
    description: Optional[str] = None
    links: Optional[Links] = None
    overrides: Optional[Overrides] = None
    id: Optional[str] = None
    type: str
    version: Optional[str] = None
    overrideTargetId: Optional[str] = None

class RangeObject(BaseModel):
    links: Optional[Links] = None
    type: str
    name: str
    id: Optional[str] = None

class FQDNObject(BaseModel):
    links: Optional[Links] = None
    type: str
    value: str
    dnsResolution: str
    overridable: Optional[bool] = None
    description: Optional[str] = None
    id: str
    name: str
    metadata: Optional[Metadata] = None