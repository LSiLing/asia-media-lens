from db import get_articles

article_keywords = {
    "economics": [
        "trade", "tariff", "gdp", "recession", "inflation", "interest", "fiscal",
        "deficit", "commodity", "equity", "monetary", "bankruptcy", "revenue",
        "austerity", "yield", "currency", "debt", "budget", "export", "import",
        "investment", "market", "stock", "oil", "energy", "supply", "demand",
        "growth", "economic", "economy", "macroeconomic", "unemployment", "wage",
        "profit", "loss", "bank", "fed", "rate", "price", "cost", "spending",
        "tax", "subsidy", "pension", "wealth", "poverty", "finance", "capital"
    ],
    "geopolitics": [
        "sanctions", "alliance", "sovereignty", "diplomacy", "conflict", "treaty",
        "bilateral", "hegemony", "summit", "tensions", "embargo", "proxy", "war",
        "military", "nuclear", "missile", "ceasefire", "nato", "un", "security",
        "threat", "power", "regime", "election", "government", "border", "territory",
        "invasion", "occupation", "troops", "army", "navy", "intelligence", "spy",
        "coup", "protest", "refugee", "humanitarian", "blockade", "deterrence",
        "geopolitical", "strategic", "foreign", "policy", "minister", "president"
    ],
    "technology": [
        "artificial intelligence", "cybersecurity", "semiconductor", "blockchain",
        "innovation", "software", "hardware", "data", "algorithm", "automation",
        "chip", "robot", "digital", "internet", "satellite", "drone", "quantum",
        "battery", "ev", "startup", "ai", "tech", "computing", "cloud", "platform",
        "app", "device", "network", "cyber", "hack", "encryption", "surveillance",
        "patent", "research", "laboratory", "science", "engineering", "space"
    ],
"society": ["health", "education", "culture", "sport", "crime", "death", "hospital", "school", "police", "court", "murder", "arrest", "cancer", "drug", "vaccine", "climate", "environment", "food", "music", "film", "art", "religion", "church", "family", "children", "women", "gender", "race", "immigration", "refugee"]

}
def classify_article(title, summary):
    words = title + ' ' + summary
    keyword_count_d = {"economics": 0, "geopolitics": 0, "technology": 0, "society": 0}
    for word in words.split():
        if word.lower() in article_keywords['technology']:
            keyword_count_d['technology'] += 1
        elif word.lower() in article_keywords['geopolitics']:
            keyword_count_d['geopolitics'] += 1
        elif word.lower() in article_keywords['economics']:
            keyword_count_d['economics'] += 1
        elif word.lower() in article_keywords['society']:
            keyword_count_d['society'] += 1

    if max(keyword_count_d.values()) == 0:
            return "other"

    return max(keyword_count_d, key=keyword_count_d.get)

if __name__ == '__main__':
    articles = get_articles()
    title = articles[1][0]
    summary = articles[1][1]
    print(classify_article(title, summary))


