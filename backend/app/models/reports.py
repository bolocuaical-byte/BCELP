"""Reports model."""
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


class Report(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "reports"

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    report_type = Column(String(100), nullable=True)
    generated_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    file_url = Column(String(1024), nullable=True)
    status = Column(String(50), nullable=True)

    project = relationship("Project")
