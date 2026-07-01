from pydantic import BaseModel
from typing import Optional


class ResearchGroupBase(BaseModel):
    name: str
    description: Optional[str] = None


class ResearchGroupCreate(ResearchGroupBase):
    pass


class ResearchGroupRead(ResearchGroupBase):
    id: str
    model_config = {"from_attributes": True}


class TestBenchBase(BaseModel):
    name: str
    location: Optional[str] = None


class TestBenchRead(TestBenchBase):
    id: str
    model_config = {"from_attributes": True}


class InstrumentBase(BaseModel):
    name: str
    model: Optional[str] = None
    serial_number: Optional[str] = None


class InstrumentRead(InstrumentBase):
    id: str
    model_config = {"from_attributes": True}


class SensorBase(BaseModel):
    name: str
    sensor_type: Optional[str] = None
    unit: Optional[str] = None


class SensorRead(SensorBase):
    id: str
    model_config = {"from_attributes": True}
