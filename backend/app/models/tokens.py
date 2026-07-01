"""Refresh token model to persist refresh token hashes."""
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


class RefreshToken(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "refresh_tokens"

    token_hash = Column(UUID(as_uuid=False), nullable=False, unique=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)
    revoked = Column(Boolean, default=False, nullable=False)

    user = relationship("User")
