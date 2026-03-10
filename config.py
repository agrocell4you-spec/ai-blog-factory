# ===============================
# RSS 뉴스 수집 설정
# ===============================

# 원하는 RSS 주소를 여기에 추가하면 됩니다.
# 여러 개 추가하면 자동으로 순회합니다.

RSS_FEEDS = [

    # Google News 한국 뉴스
    "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko",
    "https://news.google.com/rss/search?q=ai&hl=ko&gl=KR&ceid=KR:ko",

    # 기술 뉴스
    # "https://news.google.com/rss/search?q=technology",

    # 경제 뉴스
    # "https://news.google.com/rss/search?q=economy",

]

# 한 RSS에서 가져올 기사 수
ARTICLES_PER_FEED = 5
