import sqlite3
import os

DB_PATH = "ideas.db"

def create_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ideas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT
    )
    """)
    conn.commit()
    conn.close()


def run_database():
    if not os.path.exists(DB_PATH):
        create_db()

def insert_idea(title, description=None):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO ideas (title, description) VALUES (?, ?)", (title, description))
    conn.commit()
    conn.close()

def get_idea_by_id(idea_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, title, description FROM ideas WHERE id = ?", (idea_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return {"id": row[0], "title": row[1], "description": row[2]}
    else:
        return None
    
def get_all_ideas():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM ideas")
    rows = cursor.fetchall()
    conn.close()

    return rows

def delete_idea(idea_id: int):
    import sqlite3
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM ideas WHERE id = ?", (idea_id,))
    conn.commit()
    conn.close()

