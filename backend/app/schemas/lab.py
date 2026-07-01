from pydantic import BaseModel
from typing import Optional


class LabBase(BaseModel):
    name: str
    location: Optional[str] = None
    description: Optional[str] = None


class LabCreate(LabBase):
    pass


class LabUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None


class LabRead(LabBase):
    id: str

    model_config = {"from_attributes": True}
