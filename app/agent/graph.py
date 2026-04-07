from langgraph.graph import END, StateGraph

from app.agent.nodes import (
    execute_sql,
    generate_sql,
    load_schema,
    repair_sql,
    summarize,
)
from app.agent.state import AgentState


def should_repair(state: AgentState) -> str:
    if state.get("error"):
        return "repair"
    return "summarize"


def repair_success(state: AgentState) -> str:
    if state.get("error"):
        return "summarize"
    return "summarize"


def build_graph() -> StateGraph:
    graph = StateGraph(AgentState)

    graph.add_node("load_schema", load_schema)
    graph.add_node("generate_sql", generate_sql)
    graph.add_node("execute_sql", execute_sql)
    graph.add_node("repair_sql", repair_sql)
    graph.add_node("summarize", summarize)

    graph.set_entry_point("load_schema")
    graph.add_edge("load_schema", "generate_sql")
    graph.add_edge("generate_sql", "execute_sql")
    graph.add_conditional_edges("execute_sql", should_repair, {
        "repair": "repair_sql",
        "summarize": "summarize",
    })
    graph.add_edge("repair_sql", "summarize")
    graph.add_edge("summarize", END)

    return graph.compile()


agent_graph = build_graph()
