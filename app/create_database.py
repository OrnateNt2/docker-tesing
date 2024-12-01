import sqlite3

# Название базы данных
DB_NAME = "app/database.db"

# SQL-запросы для создания таблицы и добавления данных
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    info TEXT NOT NULL
);
"""

INSERT_DATA_QUERY = """
INSERT INTO data (info) VALUES
    ('Привет, мир!'),
    ('Пример данных.'),
    ('Ещё один пример.');
"""

def create_database():
    # Подключение к базе данных
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute(CREATE_TABLE_QUERY)

    # Добавление данных
    cursor.execute(INSERT_DATA_QUERY)

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()
    print(f"База данных '{DB_NAME}' успешно создана и заполнена данными.")

if __name__ == "__main__":
    create_database()
