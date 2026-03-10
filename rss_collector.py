import feedparser
from config import RSS_FEEDS, ARTICLES_PER_FEED


def collect_articles():

    articles = []

    for url in RSS_FEEDS:

        try:
            feed = feedparser.parse(url)

            for entry in feed.entries[:ARTICLES_PER_FEED]:

                articles.append({
                    "title": entry.title,
                    "summary": entry.summary
                })

        except Exception as e:
            print("RSS 오류:", e)

    return articles