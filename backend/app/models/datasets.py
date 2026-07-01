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



class Dataset(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "datasets"

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    experiment_id = Column(UUID(as_uuid=True), ForeignKey("experiments.id"), nullable=True)
    name = Column(String(512), nullable=False)
    file_path = Column(String(1024), nullable=True)
    metadata_json = Column("metadata", JSON, nullable=True)

    experiment = relationship("Experiment")


class TestRun(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "test_runs"

    experiment_id = Column(UUID(as_uuid=True), ForeignKey("experiments.id"), nullable=True)
    run_name = Column(String(255), nullable=True)
    started_at = Column(String(50), nullable=True)
    finished_at = Column(String(50), nullable=True)
    parameters = Column(JSON, nullable=True)

    experiment = relationship("Experiment")


class Result(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "results"

    test_run_id = Column(UUID(as_uuid=True), ForeignKey("test_runs.id"), nullable=True)
    metric = Column(String(255), nullable=False)
    value = Column(String(255), nullable=True)
    details = Column(JSON, nullable=True)

    test_run = relationship("TestRun")


class Report(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "reports"

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id"), nullable=True)
    title = Column(String(512), nullable=False)
    file_path = Column(String(1024), nullable=True)
    metadata_json = Column("metadata", JSON, nullable=True)

    project = relationship("Project")


