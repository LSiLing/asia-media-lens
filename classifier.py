from db import get_articles

article_keywords = { "economics": [ "inflation", "gdp", "recession", "interest rates", "fiscal", "deficit", "commodities", "equities", "bullish", "bearish", "monetary", "bankruptcy", "revenue", "austerity", "yield" ], "geopolitics": [ "sanctions", "alliance", "sovereignty", "diplomacy", "conflict", "treaty", "bilateral", "hegemony", "summit", "tensions", "embargo", "proxy", "geostrategic", "unilateral", "border" ], "technology": [ "artificial intelligence", "cybersecurity", "semiconductors", "blockchain", "innovation", "software", "hardware", "deployment", "data center", "algorithm", "automation", "disruptive", "bandwidth", "interface", "beta" ] }

def classify_article(title, summary):
    words = title + ' ' + summary
    print(words.split()[:10])
    keyword_count_d = {"economics": 0, "geopolitics": 0, "technology": 0}
    for word in words.split():
        if word.lower() in article_keywords['technology']:
            keyword_count_d['technology'] += 1
        elif word.lower() in article_keywords['geopolitics']:
            keyword_count_d['geopolitics'] += 1
        elif word.lower() in article_keywords['economics']:
            keyword_count_d['economics'] += 1

    if max(keyword_count_d.values()) == 0:
            return "other"

    return max(keyword_count_d, key=keyword_count_d.get)

if __name__ == '__main__':
    articles = get_articles()
    title = articles[1][0]
    summary = articles[1][1]
    print(classify_article(title, summary))

