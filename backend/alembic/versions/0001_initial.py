"""Initial migration

This migration uses SQLAlchemy metadata to create all tables defined in
`app.models`. It is intentionally generated to capture the current model state.

Do NOT execute this file automatically; run `alembic upgrade head` when ready.
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create all tables from SQLAlchemy metadata."""
    bind = op.get_bind()
    # Import models to ensure metadata is populated
    from app.db.base import Base
    import app.models  # noqa: F401

    Base.metadata.create_all(bind=bind)


def downgrade() -> None:
    """Drop all tables created by upgrade.

    WARNING: This will remove all data in the tables.
    """
    bind = op.get_bind()
    from app.db.base import Base
    import app.models  # noqa: F401

    Base.metadata.drop_all(bind=bind)
