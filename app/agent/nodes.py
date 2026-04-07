from app.agent.state import AgentState
from app.db.sqlite_adapter import SQLiteAdapter
from app.services.schema_loader import SchemaLoader
from app.services.sql_generator import SQLGenerator
from app.services.sql_repair import SQLRepairer
from app.services.summarizer import Summarizer

_db = SQLiteAdapter()
_schema_loader = SchemaLoader(_db)
_sql_generator = SQLGenerator()
_sql_repairer = SQLRepairer()
_summarizer = Summarizer()


def load_schema(state: AgentState) -> dict:
    schema = _schema_loader.load()
    return {"schema": schema}


def generate_sql(state: AgentState) -> dict:
    sql = _sql_generator.generate(state["schema"], state["question"])
    return {"sql": sql}


def execute_sql(state: AgentState) -> dict:
    try:
        result = _db.execute_sql(state["sql"])
        return {"result": result, "error": "", "repaired": False}
    except RuntimeError as e:
        return {"result": [], "error": str(e)}


def repair_sql(state: AgentState) -> dict:
    fixed_sql = _sql_repairer.repair(
        state["schema"], state["question"], state["sql"], state["error"]
    )
    try:
        result = _db.execute_sql(fixed_sql)
        return {"sql": fixed_sql, "result": result, "error": "", "repaired": True}
    except RuntimeError as e:
        return {"result": [], "error": str(e), "repaired": True}


def summarize(state: AgentState) -> dict:
    answer = _summarizer.summarize(
        state["question"], state["sql"], state["result"], state.get("repaired", False)
    )
    return {"answer": answer}
