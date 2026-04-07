import json

from app.llm.client import get_client, get_model
from app.llm.prompts import SUMMARIZE_PROMPT


class Summarizer:
    def summarize(
        self, question: str, sql: str, result: list[dict], repaired: bool = False
    ) -> str:
        client = get_client()
        model = get_model()
        repair_note = "注: SQL 在首次执行失败后已修复。" if repaired else ""
        prompt = SUMMARIZE_PROMPT.format(
            question=question,
            sql=sql,
            result=json.dumps(result, ensure_ascii=False, default=str),
            repair_note=repair_note,
        )
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
        )
        return resp.choices[0].message.content.strip()
