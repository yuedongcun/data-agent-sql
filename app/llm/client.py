import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(".env/local", override=True) 

_client: OpenAI | None = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(
            api_key=os.environ["OPENAI_API_KEY"],
            base_url=os.environ["OPENAI_BASE_URL"],
        )
    return _client


def get_model() -> str:
    return os.environ["OPENAI_MODEL"]
