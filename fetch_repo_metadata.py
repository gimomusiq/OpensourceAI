import requests
import time

GITHUB_API = "https://api.github.com/repos/"
HEADERS = {'Accept': 'application/vnd.github.v3+json'}


def fetch_metadata(repo_url):
    repo_path = repo_url.replace("https://github.com/", "")
    api_url = GITHUB_API + repo_path
    try:
        resp = requests.get(api_url, headers=HEADERS, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            return {
                'url': repo_url,
                'name': data.get('full_name'),
                'description': data.get('description'),
                'stars': data.get('stargazers_count'),
                'last_update': data.get('updated_at'),
                'archived': data.get('archived'),
            }
        else:
            return {'url': repo_url, 'error': f'HTTP {resp.status_code}'}
    except Exception as e:
        return {'url': repo_url, 'error': str(e)}

def main():
    with open('ai_model_repos.txt') as f:
        urls = [line.strip() for line in f if line.strip()]
    results = []
    for url in urls:
        meta = fetch_metadata(url)
        results.append(meta)
        print(meta)
        time.sleep(1.2)  # avoid GitHub API rate limits
    # Optionally, write to a file
    with open('ai_model_repos_metadata.json', 'w') as out:
        import json
        json.dump(results, out, indent=2)

if __name__ == '__main__':
    main()
