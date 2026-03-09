import requests
import json

def get_trending_keywords():
    url = "https://trends.google.com/trends/api/dailytrends"

    params = {
        "hl": "en-US",
        "tz": "-540",
        "geo": "US",
        "ns": "15"
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, params=params, headers=headers, timeout=10)
    r.raise_for_status()

    # Google returns )]}' at start
    data = json.loads(r.text[5:])

    trends = data["default"]["trendingSearchesDays"][0]["trendingSearches"]

    keywords = []
    for t in trends:
        keywords.append(t["title"]["query"])

    return keywords[:10]

