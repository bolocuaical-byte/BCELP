from alembic.config import Config
from alembic import command
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Ensure backend is on sys.path so `app` package is importable
if BASE_DIR not in sys.path:
	sys.path.insert(0, BASE_DIR)

ALEMBIC_INI = os.path.join(BASE_DIR, 'alembic.ini')

config = Config(ALEMBIC_INI)
config.set_main_option('script_location', 'alembic')

# Generate autogenerate revision
command.revision(config, message='initial_autogenerate', autogenerate=True)
print('Autogenerate revision created.')
