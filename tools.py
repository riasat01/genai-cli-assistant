import urllib.parse as parse
import urllib.request as request
from bs4 import BeautifulSoup

def search_web(query: str) -> str:
    """Searches the web for the given query and returns a summary of text results.
    Use this tool when you need up-to-date information from the internet.
    """

    try:
        encode_query = parse.quote(query)
        url = f"https://html.duckduckgo.com/html/?q={encode_query}"

        req = request.Request(
            url=url, headers={"User-Agent": "Mozilla/5.0"}
        )

        with request.urlopen(req) as response:
            html = response.read().decode("utf-8")

        soup = BeautifulSoup(html, "html.parser")
        results = []

        for result in soup.find_all("a", class_="result__snippet", limit=3):
            results.append(result.get_text().strip())

        if not results:
            return "No relevant results found."

        return "\n\n".join(results)

    except Exception as e:
        return f"Error performing search: {e}"
