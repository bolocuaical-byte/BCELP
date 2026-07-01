"""Aggregate model imports so Alembic's autogenerate discovers metadata.

Import this module early (alembic env, app startup) so `Base.metadata` contains all tables.
"""
from .base import *  # noqa: F401,F403
from .auth import *  # noqa: F401,F403
from .research import *  # noqa: F401,F403
from .people import *  # noqa: F401,F403
from .thesis import *  # noqa: F401,F403
from .lab import *  # noqa: F401,F403
from .vehicles import *  # noqa: F401,F403
from .batteries import *  # noqa: F401,F403
from .experiments import *  # noqa: F401,F403
from .datasets import *  # noqa: F401,F403
from .publications import *  # noqa: F401,F403
from .reports import *  # noqa: F401,F403
from .core_domain import *  # noqa: F401,F403
from .tokens import *  # noqa: F401,F403

__all__ = [
    # base
    "IDMixin",
    "TimestampMixin",
    "SoftDeleteMixin",
]
# Models package initialization
