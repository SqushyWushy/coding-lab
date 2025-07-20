import sqlite3
from datetime import datetime

DB_NAME = "focusbeast.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            duration INTEGER NOT NULL,
            mode TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()

def log_session(start_time, end_time, duration, mode):
    date_str = start_time.strftime("%Y-%m-%d")
    start_str = start_time.strftime("%H:%M")
    end_str = end_time.strftime("%H:%M")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sessions (date, start_time, end_time, duration, mode)
        VALUES (?, ?, ?, ?, ?)
    """, (date_str, start_str, end_str, duration, mode))

    conn.commit()
    conn.close()
