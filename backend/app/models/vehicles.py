"""Vehicle and telemetry related models."""
from sqlalchemy import Column, String, Text, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


class Vehicle(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "vehicles"

    name = Column(String(255), nullable=False)
    vin = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)

    vbox_files = relationship("VBOXFile", back_populates="vehicle")
    obd_files = relationship("OBDFile", back_populates="vehicle")


class VBOXFile(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "vbox_files"

    vehicle_id = Column(UUID(as_uuid=True), ForeignKey("vehicles.id"), nullable=True)
    file_path = Column(String(1024), nullable=False)
    metadata = Column(Text, nullable=True)

    vehicle = relationship("Vehicle", back_populates="vbox_files")


class OBDFile(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "obd_files"

    vehicle_id = Column(UUID(as_uuid=True), ForeignKey("vehicles.id"), nullable=True)
    file_path = Column(String(1024), nullable=False)
    metadata = Column(Text, nullable=True)

    vehicle = relationship("Vehicle", back_populates="obd_files")
