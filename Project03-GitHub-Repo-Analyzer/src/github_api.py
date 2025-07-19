import requests

# Optional: Add your GitHub personal token here to avoid rate limits
GITHUB_TOKEN = None  # Or: "ghp_XXXXXXXXXXXXXXXXXXXXXXXXX"

def get_repo_stats(owner, repo):
    base_url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"

    try:
        # 1. Get repo details
        repo_resp = requests.get(base_url, headers=headers)
        if repo_resp.status_code != 200:
            raise Exception(f"Repo not found or access denied. Status code: {repo_resp.status_code}")

        repo_data = repo_resp.json()

        # 2. Get contributors
        contributors_resp = requests.get(f"{base_url}/contributors", headers=headers)
        contributors_data = contributors_resp.json() if contributors_resp.status_code == 200 else []

        # 3. Get commits
        commits_resp = requests.get(f"{base_url}/commits", headers=headers, params={"per_page": 1})
        if "Link" in commits_resp.headers:
            # Get total count from pagination link
            last_page_link = [link for link in commits_resp.headers["Link"].split(',') if 'rel="last"' in link]
            if last_page_link:
                last_url = last_page_link[0].split(';')[0].strip()[1:-1]
                total_commits = int(last_url.split('=')[-1])
            else:
                total_commits = 1
        else:
            total_commits = len(commits_resp.json())

        return {
            "Name": repo_data.get("name"),
            "Owner": repo_data.get("owner", {}).get("login"),
            "Stars": repo_data.get("stargazers_count"),
            "Forks": repo_data.get("forks_count"),
            "Watchers": repo_data.get("watchers_count"),
            "Open Issues": repo_data.get("open_issues_count"),
            "Contributors": len(contributors_data),
            "Commits": total_commits
        }

    except Exception as e:
        print(f"[ERROR] {e}")
        return None


