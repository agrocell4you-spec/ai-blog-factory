from pytrends.request import TrendReq

def get_trending_keywords():
    pytrends = TrendReq()

    df = pytrends.realtime_trending_searches(pn='US')

    return df["title"].tolist()


