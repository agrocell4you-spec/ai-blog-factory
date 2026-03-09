from pytrends.request import TrendReq

def get_trending_keywords():
    pytrends = TrendReq(hl='en-US', tz=360)

    df = pytrends.trending_searches(pn='united_states')

    return df[0].tolist()[:10]
