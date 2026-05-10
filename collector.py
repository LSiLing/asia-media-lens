import feedparser
from db import insert_article, get_connection

news_dict = {"https://feeds.bbci.co.uk/news/rss.xml?edition=uk": "west",
             "https://www.theguardian.com/world/rss": "west",
             "https://news.google.com/rss/search?q=source:Reuters+macroeconomics&hl=en-US&gl=US&ceid=US:en": "west",
             "https://www.scmp.com/rss/318199/feed": "asia",
             "https://asia.nikkei.com/rss/feed/nar" : "asia",
             "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=6511": "asia",
             "https://news.google.com/rss/search?q=source):%22The+Diplomat%22&hl=en-US&gl=US&ceid=US:en": "asia"}

def collect_news():
    for k, v in news_dict.items():
        d = feedparser.parse(k)
        for entry in d.entries:
            title = entry.get("title", "none")
            summary = entry.get("summary", "none")
            url = entry.get("link", "none")
            date = entry.get("published", "none")
            insert_article(url, title, summary, date, v)

if __name__ == '__main__':
    connection, cursor = get_connection()
    collect_news()
    query = '''SELECT COUNT(*) FROM news '''
    cursor.execute(query)
    print(cursor.fetchall())