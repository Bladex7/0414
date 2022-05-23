import sqlite3

DATABASE_NAME = "db_tekkom_0414.db"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def create_table_news_0414():
    tables = [
            """CREATE TABLE IF NOT EXISTS
                tbl_students(
                    news_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL,
                    datetime TEXT NOT NULL,
                    flag TEXT NOT NULL)""" 
        ]
    db = get_db()
    cursor = db.cursor()
    
    for table in tables:
        cursor.execute(table)