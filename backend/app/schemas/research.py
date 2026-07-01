from pydantic import BaseModel
from typing import Optional


class ResearchLineBase(BaseModel):
    title: str
    summary: Optional[str] = None


class ResearchLineCreate(ResearchLineBase):
    project_id: Optional[str] = None


class ResearchLineUpdate(BaseModel):
    title: Optional[str] = None
    summary: Optional[str] = None


class ResearchLineRead(ResearchLineBase):
    id: str
    project_id: Optional[str] = None

    model_config = {"from_attributes": True}
