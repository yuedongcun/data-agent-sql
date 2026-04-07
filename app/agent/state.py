from __future__ import annotations

from typing import Annotated, Any

from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    question: str
    schema: str
    sql: str
    result: list[dict[str, Any]]
    error: str
    repaired: bool
    answer: str
