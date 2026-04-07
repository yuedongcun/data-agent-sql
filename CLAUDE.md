# CLAUDE.md

## 项目目标

这是一个最小版的 `data-agent-sql` 项目。

当前阶段目标不是做完整的 RAG + Agent 系统，而是先做一个最小可运行版本，打通这条主链路：

**用户问题 -> 读取数据库 schema -> 生成 SQL -> 执行 SQL -> 返回结果 -> 执行失败时尝试修复 SQL**

当前版本**不使用向量数据库**，不接入 Qdrant / Chroma，不做 retrieval，不做 multi-agent，不做 MySQL，不做前端页面。

---

## 当前版本范围

### 要做
- 使用 FastAPI 提供最小 API
- 使用 SQLite 作为数据库
- 使用 OpenAI-compatible 接口调用模型（当前通过 OpenRouter）
- 使用 LangGraph 组织最小 workflow
- 支持：
  - 自然语言转 SQL
  - SQL 执行
  - 出错后修复一次
  - 返回结果、SQL、是否修复

### 不做
- 不做向量数据库
- 不做 RAG 检索
- 不做 MySQL
- 不做分布式
- 不做 multi-agent
- 不做复杂评测
- 不做前端 UI

---

## 技术栈

- Python 3.11
- FastAPI
- LangGraph
- SQLite
- OpenAI Python SDK（通过 OpenRouter 的 base_url 使用）
- Pydantic

---

## 项目结构

```text
data-agent-sql/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── agent/
│   │   ├── graph.py
│   │   ├── state.py
│   │   └── nodes.py
│   ├── db/
│   │   ├── base.py
│   │   └── sqlite_adapter.py
│   ├── llm/
│   │   ├── client.py
│   │   └── prompts.py
│   └── services/
│       ├── schema_loader.py
│       ├── sql_generator.py
│       ├── sql_repair.py
│       └── summarizer.py
├── data/
│   ├── demo.db
│   └── schema.sql
├── tests/
├── .env
├── requirements.txt
└── README.md
