"""Database bootstrap helpers."""

from __future__ import annotations

from pathlib import Path
import sqlite3


DB_PATH = Path("database") / "atc_operation_manager.sqlite3"


def get_connection() -> sqlite3.Connection:
    """Return a SQLite connection, creating the database file if needed."""
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)
