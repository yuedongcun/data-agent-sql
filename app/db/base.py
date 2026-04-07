from abc import ABC, abstractmethod


class DatabaseAdapter(ABC):
    @abstractmethod
    def execute_sql(self, sql: str) -> list[dict]:
        """Execute a SELECT statement and return rows as dicts."""
        ...

    @abstractmethod
    def get_schema(self) -> str:
        """Return the DDL schema of all tables."""
        ...
