import requests
from bs4 import BeautifulSoup

def search(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(f"https://duckduckgo.com/html/?q={query}", headers=headers)

    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for result in soup.find_all("a", class_="result__a"):
        results.append({
            "title": result.text,
            "url": result["href"],
        })

    return results
