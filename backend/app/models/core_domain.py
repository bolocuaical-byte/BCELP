"""Core domain models: research groups, instruments, sensors, test benches."""
from sqlalchemy import Column, String, Text, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


class ResearchGroup(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "research_groups"

    name = Column(String(255), nullable=False, unique=True)
    description = Column(Text, nullable=True)
    lead_id = Column(UUID(as_uuid=True), ForeignKey("researchers.id"), nullable=True)

    members = relationship("Researcher", back_populates="group")


class TestBench(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "test_benches"

    name = Column(String(255), nullable=False)
    location = Column(String(255), nullable=True)
    lab_id = Column(UUID(as_uuid=True), ForeignKey("laboratories.id"), nullable=True)

    laboratory = relationship("Laboratory")
    instruments = relationship("Instrument", back_populates="test_bench")


class Instrument(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "instruments"

    name = Column(String(255), nullable=False)
    model = Column(String(255), nullable=True)
    serial_number = Column(String(255), nullable=True)
    equipment_id = Column(UUID(as_uuid=True), ForeignKey("equipment.id"), nullable=True)
    test_bench_id = Column(UUID(as_uuid=True), ForeignKey("test_benches.id"), nullable=True)

    equipment = relationship("Equipment")
    test_bench = relationship("TestBench", back_populates="instruments")
    sensors = relationship("Sensor", back_populates="instrument")


class Sensor(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "sensors"

    name = Column(String(255), nullable=False)
    sensor_type = Column(String(255), nullable=True)
    unit = Column(String(64), nullable=True)
    instrument_id = Column(UUID(as_uuid=True), ForeignKey("instruments.id"), nullable=True)

    instrument = relationship("Instrument", back_populates="sensors")
