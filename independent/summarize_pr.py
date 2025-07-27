import requests
import json

url = "http://localhost:11434/api/generate"
payload = {
    "model": "gemma:2b",
    "prompt": "Summarize the following PR: Added login, logout, and session management."
}

response = requests.post(url, json=payload, stream=True)

full_output = ""
for line in response.iter_lines():
    if line:
        data = json.loads(line)
        full_output += data.get("response", "")

print("\nFull Response:\n", full_output)
