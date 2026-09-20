import requests
from bs4 import BeautifulSoup
from langchain.tools import tool

@tool
def scrape_urls(url_links:list[str]):
    """
    Scrape textual content from a list of webpage URLs.

    Args:
        urls (list[str]): A list of URLs to fetch and extract content from.
    """
    results = []

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    for url in url_links:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            for tag in soup(["script", "style", "nav", "footer"]):
                tag.decompose()

            text = soup.get_text(" ", strip=True)

            results.append({
                "url": url,
                "content": text[0:1000]
            })

        except Exception as e:
            results.append({
                "url": url,
                "error": str(e)
            })

    return results