from __future__ import annotations

from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.agent.graph import agent_graph

router = APIRouter(prefix="/api", tags=["agent"])


class QueryRequest(BaseModel):
    question: str = Field(..., min_length=1, description="用户自然语言问题")


class QueryResponse(BaseModel):
    question: str
    sql: str
    result: list[dict[str, Any]]
    answer: str
    repaired: bool


@router.post("/query", response_model=QueryResponse)
async def query(req: QueryRequest) -> QueryResponse:
    result = agent_graph.invoke({
        "question": req.question,
        "messages": [],
        "schema": "",
        "sql": "",
        "result": [],
        "error": "",
        "repaired": False,
        "answer": "",
    })
    return QueryResponse(
        question=result["question"],
        sql=result["sql"],
        result=result["result"],
        answer=result["answer"],
        repaired=result["repaired"],
    )
