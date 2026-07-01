"""Battery domain models: cells, packs and BMS."""
from sqlalchemy import Column, String, Text, ForeignKey, Integer, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


class BatteryCell(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "battery_cells"

    serial = Column(String(255), nullable=True)
    chemistry = Column(String(100), nullable=True)
    nominal_capacity_ah = Column(Float, nullable=True)
    nominal_voltage = Column(Float, nullable=True)
    manufacturer = Column(String(255), nullable=True)

    pack_id = Column(UUID(as_uuid=True), ForeignKey("battery_packs.id"), nullable=True)
    pack = relationship("BatteryPack", back_populates="cells")


class BatteryPack(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "battery_packs"

    name = Column(String(255), nullable=True)
    nominal_voltage = Column(Float, nullable=True)
    nominal_capacity_ah = Column(Float, nullable=True)

    cells = relationship("BatteryCell", back_populates="pack")
    bms_units = relationship("BMS", back_populates="pack")


class BMS(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "bms"

    pack_id = Column(UUID(as_uuid=True), ForeignKey("battery_packs.id"), nullable=True)
    firmware_version = Column(String(100), nullable=True)
    manufacturer = Column(String(255), nullable=True)

    pack = relationship("BatteryPack", back_populates="bms_units")
