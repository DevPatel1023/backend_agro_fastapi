"""

Database setup - SQLite via aiosqlite

"""

import aiosqlite
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

DB_PATH = Path("data/crop_disease.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)


async def get_db():
    async with aiosqlite.connect(DB_PATH) as db:
        db.row_factory = aiosqlite.Row
        yield db



async def init_db():
    pass