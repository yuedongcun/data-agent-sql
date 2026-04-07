SQL_GENERATION_PROMPT = """你是一个 SQL 专家。根据以下数据库 schema 和用户问题，生成一个正确的 SQLite SQL 查询。

数据库 Schema:
{schema}

用户问题: {question}

要求:
- 只输出一条 SQL，不要解释
- 只输出 SELECT 查询
- 不要用 markdown 包裹"""

SQL_REPAIR_PROMPT = """你是一个 SQL 专家。以下 SQL 执行失败了，请修复它。

数据库 Schema:
{schema}

用户问题: {question}

原始 SQL:
{sql}

错误信息:
{error}

要求:
- 只输出修复后的 SQL，不要解释
- 只输出 SELECT 查询
- 不要用 markdown 包裹"""

SUMMARIZE_PROMPT = """根据用户问题和查询结果，用简洁的中文回答用户问题。

用户问题: {question}

执行 SQL: {sql}

查询结果:
{result}

{repair_note}

请用 1-3 句话回答。"""
