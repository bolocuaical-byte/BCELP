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


class EquipmentBase(BaseModel):
    name: str
    serial_number: Optional[str] = None
    model: Optional[str] = None
    manufacturer: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    laboratory_id: Optional[str] = None


class EquipmentCreate(EquipmentBase):
    pass


class EquipmentUpdate(BaseModel):
    name: Optional[str] = None
    serial_number: Optional[str] = None
    model: Optional[str] = None
    manufacturer: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None


class EquipmentRead(EquipmentBase):
    id: str

    model_config = {"from_attributes": True}


class InstrumentBase(BaseModel):
    name: str
    model: Optional[str] = None
    manufacturer: Optional[str] = None
    serial_number: Optional[str] = None
    metadata: Optional[dict] = None


class InstrumentCreate(InstrumentBase):
    equipment_id: str


class InstrumentRead(InstrumentBase):
    id: str

    model_config = {"from_attributes": True}


class SensorBase(BaseModel):
    name: str
    sensor_type: Optional[str] = None
    unit: Optional[str] = None
    calibration_metadata: Optional[dict] = None


class SensorCreate(SensorBase):
    instrument_id: str


class SensorRead(SensorBase):
    id: str

    model_config = {"from_attributes": True}


class CalibrationRecordRead(BaseModel):
    id: str
    sensor_id: str
    performed_at: Optional[str] = None
    performed_by: Optional[str] = None
    result: Optional[dict] = None
    next_due: Optional[str] = None

    model_config = {"from_attributes": True}


class MaintenanceRecordRead(BaseModel):
    id: str
    equipment_id: str
    performed_at: Optional[str] = None
    performed_by: Optional[str] = None
    notes: Optional[str] = None
    is_planned: Optional[bool] = None

    model_config = {"from_attributes": True}


class EquipmentReservationRead(BaseModel):
    id: str
    equipment_id: str
    user_id: Optional[str] = None
    start_at: Optional[str] = None
    end_at: Optional[str] = None
    purpose: Optional[str] = None
    status: Optional[str] = None

    model_config = {"from_attributes": True}


class EquipmentDocumentRead(BaseModel):
    id: str
    equipment_id: str
    filename: str
    url: Optional[str] = None
    uploaded_at: Optional[str] = None

    model_config = {"from_attributes": True}
