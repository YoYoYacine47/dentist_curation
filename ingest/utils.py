from sqlalchemy import create_engine
from django.conf import settings

# accessing database:
engine = create_engine(
    f"mysql://{settings.DB_SETTINGS['USER']}@{settings.DB_SETTINGS['HOST']}/{settings.DB_SETTINGS['NAME']}")
conn = engine.connect()
