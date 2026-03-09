import feedparser

def get_news(keyword):

    url = f"https://news.google.com/rss/search?q={keyword}"

    feed = feedparser.parse(url)

    articles = []

    for entry in feed.entries[:3]:

        articles.append({
            "title": entry.title,
            "summary": entry.summary
        })

    return articles