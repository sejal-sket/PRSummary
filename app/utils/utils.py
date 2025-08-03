import requests

def build_prompt(title, description, file_changes):
    prompt = f"""
You are a senior software engineer reviewing a GitHub Pull Request.

## PR Title:
{title}

## PR Description:
{description}

## Files Changed:
{file_changes}

### Task:
Please analyze this PR and provide the following:
1. A brief summary of what this PR does.
2. The quality of the description — is it clear, complete, and understandable?
3. Any obvious issues in the changes, such as naming, missing tests, or code smells.
4. Suggestions for improvement, if any.
5. Is this PR ready to be merged? (yes/no) and why.

Respond clearly and concisely as if you're submitting review notes.
"""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "gemma:2b", "prompt": prompt, "stream": False}
    )
    response.raise_for_status()
    return response.json()["response"]
