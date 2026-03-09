import requests
import xml.etree.ElementTree as ET

def get_trending_keywords():
    url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    root = ET.fromstring(response.content)

    keywords = []

    for item in root.findall(".//item"):
        title = item.find("title").text
        keywords.append(title)

    return keywords[:10]
