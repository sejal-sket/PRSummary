import re
import requests
from flask import Blueprint, request, jsonify

review_bp = Blueprint('review', __name__)

@review_bp.route('/review', methods=['POST'])
def review_pr():
    try:
        data = request.get_json()
        pr_url = data.get('pr_url')

        if not pr_url:
            return jsonify({"error": "Missing 'pr_url' in request body."}), 400

        match = re.match(r'https://github\.com/([^/]+)/([^/]+)/pull/(\d+)', pr_url)
        if not match:
            return jsonify({"error": "Invalid GitHub PR URL format."}), 400

        owner, repo, pr_number = match.groups()

        # Optional: GitHub token for private repos or more rate limit
        headers = {
            "Accept": "application/vnd.github.v3+json",
            # "Authorization": "Bearer YOUR_GITHUB_TOKEN"
        }

        pr_api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}"
        pr_response = requests.get(pr_api_url, headers=headers)
        pr_response.raise_for_status()
        pr_data = pr_response.json()

        # Optionally, get list of files changed:
        files_url = pr_data.get("url") + "/files"
        files_response = requests.get(files_url, headers=headers)
        files_response.raise_for_status()
        files_data = files_response.json()

        return jsonify({
            "title": pr_data.get("title"),
            "description": pr_data.get("body"),
            "diff_url": pr_data.get("diff_url"),
            "files": [f["filename"] for f in files_data]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
