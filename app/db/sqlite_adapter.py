import sqlite3
from pathlib import Path

from app.db.base import DatabaseAdapter


class SQLiteAdapter(DatabaseAdapter):
    def __init__(self, db_path: str | Path = "data/demo.db"):
        self.db_path = str(db_path)

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def execute_sql(self, sql: str) -> list[dict]:
        with self._connect() as conn:
            try:
                rows = conn.execute(sql).fetchall()
                return [dict(r) for r in rows]
            except sqlite3.Error as e:
                raise RuntimeError(f"SQL execution error: {e}") from e

    def get_schema(self) -> str:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
            ).fetchall()
            return "\n\n".join(r["sql"] for r in rows if r["sql"])
