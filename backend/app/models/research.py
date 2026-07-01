"""Research-related models: projects and research lines."""
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


class Project(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "projects"

    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    status = Column(String(50), nullable=True, default="draft")

    research_lines = relationship("ResearchLine", back_populates="project")


class ResearchLine(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "research_lines"

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=False)
    title = Column(String(255), nullable=False)
    summary = Column(Text, nullable=True)

    project = relationship("Project", back_populates="research_lines")
