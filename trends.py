from pytrends.request import TrendReq

def get_trending_keywords():

    pytrends = TrendReq()

    trends = pytrends.trending_searches(pn='united_states')

    keywords = trends[0].tolist()

    return keywords[:20]