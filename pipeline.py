from db import get_unanalyzed_articles, update_article, get_connection
from nlp import analyze_article
from classifier import classify_article

def run_pipeline():
    articles = get_unanalyzed_articles()
    for article in articles:
        title = article[0]
        summary = article[1]
        id = article[3]
        analyzed_article = analyze_article(title, summary)
        category = classify_article(title, summary)
        sentiment = analyzed_article['sentiment']["compound"]

        updated_article = update_article(sentiment, category, id)

if __name__ == '__main__':
    connection, cursor = get_connection()
    run_pipeline()
    query = '''SELECT COUNT(*) FROM news
 WHERE news.sentiment IS NOT NULL AND news.category IS NOT NULL'''
    cursor.execute(query)
    print(cursor.fetchall())