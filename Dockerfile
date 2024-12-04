FROM python:3.10-slim

# Установить рабочую директорию
WORKDIR /usr/src/app

# Установить зависимости системы и SQLite
RUN apt-get update && apt-get install -y sqlite3 && rm -rf /var/lib/apt/lists/*

# Скопировать зависимости и установить их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать файлы приложения
COPY . .

# Убедиться, что папка для базы данных существует
RUN mkdir -p /usr/src/app/data

# Инициализация базы данных
RUN python app/init_db.py

# Открыть порт для бота
EXPOSE 8080

# Запуск приложения
CMD ["python", "app/bot.py"]
