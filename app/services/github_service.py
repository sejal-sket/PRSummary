import os
import re
import requests

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")  # 👈 set via env variable

def fetch_pr_details(pr_url: str):
    match = re.match(r'https://github\.com/([^/]+)/([^/]+)/pull/(\d+)', pr_url)
    if not match:
        raise ValueError("Invalid PR URL format")

    owner, repo, pr_number = match.groups()
    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'
    if not GITHUB_TOKEN:
        print("⚠️  Warning: No GITHUB_TOKEN found. Requests may fail for private repos or rate-limit sooner.")

    pr_response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}",
        headers=headers
    )
    pr_response.raise_for_status()
    pr_data = pr_response.json()

    files_response = requests.get(
        f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files",
        headers=headers
    )
    files_response.raise_for_status()
    files_data = files_response.json()

    title = pr_data.get("title", "")
    description = pr_data.get("body") or "No description provided."
    file_changes = "\n".join([
        f"- {file.get('filename')}: {file.get('status')}"
        for file in files_data
    ])

    return title, description, file_changes
