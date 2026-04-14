import requests
from concurrent.futures import ThreadPoolExecutor

def check_url(url):
    try:
        resp = requests.head(url, allow_redirects=True, timeout=5)
        return url, resp.status_code == 200
    except Exception:
        return url, False

def main():
    with open('ai_model_repos.txt') as f:
        urls = [line.strip() for line in f if line.strip()]
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url, ok in executor.map(check_url, urls):
            results.append((url, ok))
    for url, ok in results:
        print(f'{url} - {"OK" if ok else "NOT AVAILABLE"}')

if __name__ == '__main__':
    main()
