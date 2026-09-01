import sqlite3

# Создает файл базы данных database.db прямо в папке проекта
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Создаем таблицу сессий калькулятора
cursor.execute("""
CREATE TABLE IF NOT EXISTS calculator_sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    monthly_visitors INTEGER,
    average_order_value REAL,
    current_orders INTEGER,
    estimated_lost_revenue REAL,
    conservative_recovered REAL,
    base_recovered REAL,
    optimistic_recovered REAL
)
""")

connection.commit()
connection.close()
print("База данных SQLite успешно создана и таблица готова!")