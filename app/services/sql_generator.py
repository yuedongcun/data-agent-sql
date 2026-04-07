from app.llm.client import get_client, get_model
from app.llm.prompts import SQL_GENERATION_PROMPT


class SQLGenerator:
    def generate(self, schema: str, question: str) -> str:
        client = get_client()
        model = get_model()
        prompt = SQL_GENERATION_PROMPT.format(schema=schema, question=question)
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        return resp.choices[0].message.content.strip()
