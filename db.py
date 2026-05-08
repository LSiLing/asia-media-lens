import sqlite3

def get_connection():

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    return connection, cursor

def create_table(connection, cursor):

    command = '''CREATE TABLE IF NOT EXISTS news(news_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    url TEXT, title TEXT, summary TEXT, date TEXT, tag TEXT, sentiment FLOAT, category TEXT)'''
    cursor.execute(command)
    connection.commit()

def insert_article(url, title, summary, date, tag):
    connection, cursor = get_connection()

    query = ('''INSERT INTO news (url, title, summary, date, tag, sentiment, category) VALUES (?, ?, ?, ?, ?, ?, ?)''')
    cursor.execute(query, (url, title, summary, date, tag, None, None))
    connection.commit()

def get_articles():
    connection, cursor = get_connection()

    query = '''SELECT news.title, news.summary, news.tag FROM news'''
    cursor.execute(query)
    return cursor.fetchall()

def update_article(sentiment, category, news_id):
    connection, cursor = get_connection()

    query = '''UPDATE news 
            SET sentiment = ?, category = ?
             WHERE news_id = ?'''
    cursor.execute(query, (sentiment, category, news_id))
    connection.commit()

def get_unanalyzed_articles():
    connection, cursor = get_connection()
    query = '''SELECT news.title, news.summary, news.tag, news.news_id
    FROM news
     WHERE news.sentiment IS NULL AND news.category IS NULL'''
    cursor.execute(query)
    return cursor.fetchall()



if __name__ == '__main__':
   connection, cursor = get_connection()
   create_table(connection, cursor)
