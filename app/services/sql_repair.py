from app.llm.client import get_client, get_model
from app.llm.prompts import SQL_REPAIR_PROMPT


class SQLRepairer:
    def repair(self, schema: str, question: str, sql: str, error: str) -> str:
        client = get_client()
        model = get_model()
        prompt = SQL_REPAIR_PROMPT.format(
            schema=schema, question=question, sql=sql, error=error
        )
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        return resp.choices[0].message.content.strip()
