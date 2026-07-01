"""Laboratory models: equipment, inventory and maintenance."""
from sqlalchemy import Column, String, Text, ForeignKey, Integer
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
    location = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    laboratory_id = Column(UUID(as_uuid=True), ForeignKey("laboratories.id"), nullable=True)

    inventory_items = relationship("InventoryItem", back_populates="equipment")
    laboratory = relationship("Laboratory", back_populates="equipment")


class InventoryItem(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "inventory_items"

    equipment_id = Column(UUID(as_uuid=True), ForeignKey("equipment.id"), nullable=True)
    quantity = Column(Integer, nullable=False, default=1)
    condition = Column(String(100), nullable=True)

    equipment = relationship("Equipment", back_populates="inventory_items")


class MaintenanceEvent(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "maintenance_events"

    equipment_id = Column(UUID(as_uuid=True), ForeignKey("equipment.id"), nullable=False)
    description = Column(Text, nullable=True)
    performed_by = Column(String(255), nullable=True)
    scheduled_at = Column(String(50), nullable=True)

    equipment = relationship("Equipment")
