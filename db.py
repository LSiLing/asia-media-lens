import sqlite3

def get_connection():

    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    return connection, cursor

def create_table(connection, cursor):

    command = '''CREATE TABLE IF NOT EXISTS news(news_id INTEGER PRIMARY KEY AUTOINCREMENT, 
    url TEXT, title TEXT, summary TEXT, date TEXT, tags TEXT)'''
    cursor.execute(command)
    connection.commit()

if __name__ == '__main__':
   connection, cursor = get_connection()
   create_table(connection, cursor)