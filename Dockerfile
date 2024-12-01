# Базовый образ
FROM python:3.10-slim

# Установить рабочую директорию
WORKDIR /usr/src/app

# Скопировать зависимости и установить их
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Скопировать приложение
COPY . .

# Убедитесь, что папка для базы данных существует
RUN mkdir -p /usr/src/app/data

# Открыть порт для бота
EXPOSE 8080

# Запустить бота
CMD ["python", "app/bot.py"]
