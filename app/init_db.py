import sqlite3

DB_PATH = "/usr/src/app/data/database.db"

def initialize_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Создание таблицы, если её нет
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        info TEXT NOT NULL
    );
    """)

    # Добавление тестовых данных (опционально)
    cursor.execute("INSERT INTO data (info) VALUES (?)", ("Пример данных",))

    conn.commit()
    conn.close()
    print("База данных инициализирована.")

if __name__ == "__main__":
    initialize_database()
