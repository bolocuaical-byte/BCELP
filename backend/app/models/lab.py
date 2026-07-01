"""Laboratory models: equipment, instruments, sensors, calibration and maintenance."""
from datetime import datetime

from sqlalchemy import Column, String, Text, ForeignKey, Integer, DateTime, Boolean, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


class Laboratory(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "laboratories"

    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)

    equipment = relationship("Equipment", back_populates="laboratory")


class Equipment(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "equipment"

    name = Column(String(255), nullable=False)
    serial_number = Column(String(255), nullable=True)
    model = Column(String(255), nullable=True)
    manufacturer = Column(String(255), nullable=True)
    location = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    laboratory_id = Column(UUID(as_uuid=True), ForeignKey("laboratories.id"), nullable=True)

    inventory_items = relationship("InventoryItem", back_populates="equipment")
    laboratory = relationship("Laboratory", back_populates="equipment")
    instruments = relationship("Instrument", back_populates="equipment")
    documents = relationship("EquipmentDocument", back_populates="equipment")


class Instrument(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "instruments"

    equipment_id = Column(UUID(as_uuid=True), ForeignKey("equipment.id"), nullable=False)
    name = Column(String(255), nullable=False)
    model = Column(String(255), nullable=True)
    manufacturer = Column(String(255), nullable=True)
    serial_number = Column(String(255), nullable=True)
    metadata = Column(JSON, nullable=True)

    equipment = relationship("Equipment", back_populates="instruments")
    sensors = relationship("Sensor", back_populates="instrument")


class Sensor(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "sensors"

    instrument_id = Column(UUID(as_uuid=True), ForeignKey("instruments.id"), nullable=False)
    name = Column(String(255), nullable=False)
    sensor_type = Column(String(100), nullable=True)
    unit = Column(String(50), nullable=True)
    calibration_metadata = Column(JSON, nullable=True)

    instrument = relationship("Instrument", back_populates="sensors")


class CalibrationRecord(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "calibration_records"

    sensor_id = Column(UUID(as_uuid=True), ForeignKey("sensors.id"), nullable=False)
    performed_at = Column(DateTime, default=datetime.utcnow)
    performed_by = Column(String(255), nullable=True)
    result = Column(JSON, nullable=True)
    next_due = Column(DateTime, nullable=True)

    sensor = relationship("Sensor")


class MaintenanceRecord(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "maintenance_records"

    equipment_id = Column(UUID(as_uuid=True), ForeignKey("equipment.id"), nullable=False)
    performed_at = Column(DateTime, default=datetime.utcnow)
    performed_by = Column(String(255), nullable=True)
    notes = Column(Text, nullable=True)
    is_planned = Column(Boolean, default=False)

    equipment = relationship("Equipment")


class EquipmentReservation(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "equipment_reservations"

    equipment_id = Column(UUID(as_uuid=True), ForeignKey("equipment.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), nullable=True)
    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=False)
    purpose = Column(Text, nullable=True)
    status = Column(String(50), nullable=True)

    equipment = relationship("Equipment")


class EquipmentDocument(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "equipment_documents"

    equipment_id = Column(UUID(as_uuid=True), ForeignKey("equipment.id"), nullable=False)
    filename = Column(String(255), nullable=False)
    url = Column(String(1024), nullable=True)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    equipment = relationship("Equipment", back_populates="documents")
