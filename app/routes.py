from flask import Blueprint, request, jsonify
import requests

summarize_bp = Blueprint('summarize', __name__)

def query_local_llm(prompt):
    try:
        response = requests.post(
            'http://localhost:11434/api/generate',
            json={
                "model": "mistral",
                "prompt": prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json()["response"]
    except Exception as e:
        return f"Error contacting local LLM: {str(e)}"

@summarize_bp.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    pr_content = data.get("pr_content", "")

    if not pr_content:
        return jsonify({"error": "Missing 'pr_content' field"}), 400

    prompt = f"Summarize the following GitHub Pull Request:\n\n{pr_content}"
    summary = query_local_llm(prompt)

    return jsonify({"summary": summary})
