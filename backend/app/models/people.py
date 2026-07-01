"""People models: researchers, students, advisors."""
from sqlalchemy import Column, String, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


class Researcher(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "researchers"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    affiliation = Column(String(255), nullable=True)
    bio = Column(Text, nullable=True)

    user = relationship("User")


class Student(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "students"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    program = Column(String(255), nullable=True)
    enrollment_year = Column(String(10), nullable=True)

    user = relationship("User")


class Advisor(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "advisors"

    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)
    department = Column(String(255), nullable=True)

    user = relationship("User")
