from flask import Blueprint, request, jsonify
from app.services.github_service import fetch_pr_details
from app.services.ollama_service import get_ollama_response

bp = Blueprint("routes", __name__)

@bp.route('/analyze', methods=['POST'])
def analyze_pr():
    try:
        data = request.json
        pr_url = data.get('pr_url')
        title, description, file_changes = fetch_pr_details(pr_url)
        summary = get_ollama_response(title, description, file_changes)
        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": f"❌ Error: {str(e)}"}), 500
