from app.db.sqlite_adapter import SQLiteAdapter


class SchemaLoader:
    def __init__(self, db: SQLiteAdapter):
        self.db = db

    def load(self) -> str:
        return self.db.get_schema()
