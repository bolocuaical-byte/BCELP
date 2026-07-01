"""Thesis related model."""
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


class Thesis(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "theses"

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"), nullable=True)
    advisor_id = Column(UUID(as_uuid=True), ForeignKey("advisors.id"), nullable=True)
    title = Column(String(512), nullable=False)
    abstract = Column(Text, nullable=True)
    version = Column(String(50), nullable=True)

    project = relationship("Project")
    student = relationship("Student")
    advisor = relationship("Advisor")
