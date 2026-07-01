"""Publications, authors and journals."""
from sqlalchemy import Column, String, Text, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.db.base import Base
from .base import IDMixin, TimestampMixin, SoftDeleteMixin


publication_authors = Table(
    "publication_authors",
    Base.metadata,
    Column("publication_id", UUID(as_uuid=True), ForeignKey("publications.id"), primary_key=True),
    Column("author_id", UUID(as_uuid=True), ForeignKey("authors.id"), primary_key=True),
)


class Journal(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "journals"

    name = Column(String(512), nullable=False)
    issn = Column(String(50), nullable=True)


class Author(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "authors"

    full_name = Column(String(255), nullable=False)
    affiliation = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)

    publications = relationship("Publication", secondary=publication_authors, back_populates="authors")


class Publication(Base, IDMixin, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "publications"

    title = Column(String(1024), nullable=False)
    abstract = Column(Text, nullable=True)
    journal_id = Column(UUID(as_uuid=True), ForeignKey("journals.id"), nullable=True)
    published_at = Column(String(50), nullable=True)

    journal = relationship("Journal")
    authors = relationship("Author", secondary=publication_authors, back_populates="publications")
