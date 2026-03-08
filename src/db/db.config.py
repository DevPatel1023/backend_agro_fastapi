"""

Database setup - SQLite via aiosqlite(local, no setup)

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
    ''' create all tables. '''
    async with aiosqlite.connect(DB_PATH) as db:
        await db.executescript("""
            CREATE TABLE IF NOT EXISTS predictions (
                id  INTEGER PRIMARY KEY AUTPINCREMENT,
                image_path TEXT,
                plant TEXT,
                diseases TEXT,  -- json array of {label, confidence}
                is_unknown INTEGER DEFAULT 0,
                gradcam_path TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
                               
            
            CREATE TABLE IF NOT EXISTS review_queue (
                id INTEGER PRIMARY KEY AUTOINCREMEMT,
                prediction_id INTEGER REFRENCES predictions(id),
                image_path TEXT NOT NULL,
                reason TEXT, -- e.g. "low confidence"
                status TEXT DEFAULT 'pending', -- pending | labeled | rejected
                expert_label TEXT, -- json: {plant, disease:[]}
                labeled_by TEXT,
                created_at TEXT,
                labeled_at TIMESTAMP
                );
                               

            CREATE TABLE IF NOT EXISTS model_versions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                version TEXT NOT NULL,
                model_type TEXT NOT NULL,
                accuracy TEXT,
                notes REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                created_at TIMESTAMP
                );
        """)
        await db.commit()
        logger.info("tabels ready: predictions, review_queue, model versions")
