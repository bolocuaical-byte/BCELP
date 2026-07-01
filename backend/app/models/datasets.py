"""Dataset models: CSV, VBOX and OBD metadata storage."""
from sqlalchemy import Column, String, Text, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


class CSVDataset(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "csv_datasets"

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    file_path = Column(String(1024), nullable=False)
    schema = Column(JSON, nullable=True)


class VBOXFile(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "vbox_files"

    vehicle_id = Column(UUID(as_uuid=True), ForeignKey("vehicles.id"), nullable=True)
    file_path = Column(String(1024), nullable=False)
    metadata = Column(JSON, nullable=True)


class OBDFile(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "obd_files"

    vehicle_id = Column(UUID(as_uuid=True), ForeignKey("vehicles.id"), nullable=True)
    file_path = Column(String(1024), nullable=False)
    metadata = Column(JSON, nullable=True)
