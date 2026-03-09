import feedparser

def get_trending_keywords():
    # 1. 경향신문 전체기사 RSS (한글 블로그용)
    rss_url = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
    

    try:
        # RSS 주소에서 뉴스 정보를 읽어옵니다.
        feed = feedparser.parse(rss_url)
        
        # 만약 가져온 데이터가 비어있다면
        if not feed.entries:
            print("RSS 데이터를 찾을 수 없습니다. 주소를 확인해주세요.")
            return ["최신 사회 이슈", "오늘의 경제 지표", "실시간 주요 뉴스"]

        keywords = []
        for entry in feed.entries:
            # 뉴스 제목(Title)을 가져옵니다.
            keywords.append(entry.title)
            
        # 최신 뉴스 제목 10개만 반환합니다.
        return keywords[:10]

    except Exception as e:
        print(f"RSS 읽기 중 오류 발생: {e}")
        return ["뉴스 데이터 수집 중", "실시간 뉴스 업데이트", "최신 트렌드 요약"]

if __name__ == "__main__":
    # 테스트 실행
    print(get_trending_keywords())


