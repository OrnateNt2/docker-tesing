# Базовый образ
FROM python:3.10-slim

# Установить рабочую директорию
WORKDIR /usr/src/app

# Скопировать зависимости и установить их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать все файлы
COPY . .

# Открыть порт для бота
EXPOSE 8080

# Запустить бота
CMD ["python", "app/bot.py"]
