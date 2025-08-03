import requests
from app.utils.utils import build_prompt

def get_ollama_response(title: str, description: str, file_changes: str) -> str:
    prompt = build_prompt(title, description, file_changes)

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "gemma:2b",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False
        }
    )
    response.raise_for_status()
    return response.json()["message"]["content"]
