"""Experiment and test session models."""
from sqlalchemy import Column, String, Text, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


class Experiment(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "experiments"

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    metadata = Column(JSON, nullable=True)

    test_sessions = relationship("TestSession", back_populates="experiment")


class TestSession(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "test_sessions"

    experiment_id = Column(UUID(as_uuid=True), ForeignKey("experiments.id"), nullable=False)
    session_name = Column(String(255), nullable=True)
    parameters = Column(JSON, nullable=True)
    results = Column(JSON, nullable=True)

    experiment = relationship("Experiment", back_populates="test_sessions")
