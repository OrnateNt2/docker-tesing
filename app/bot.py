from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import sqlite3

# Укажите токен вашего бота
BOT_TOKEN = "5729193808:AAFfQaNQ_CXMslH7WpDgSP90_rYTfV0CIbc"
#test
DB_PATH = "/usr/src/app/data/database.db"
# Функция для получения данных из базы
def get_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Обработчик команды /start
def start(update: Update, context: CallbackContext):
    data = get_data()
    if data:
        response = "\n".join([f"{row[0]}: {row[1]}" for row in data])
    else:
        response = "Данных в базе пока нет."
    update.message.reply_text(response)

def main():
    # Создаем Updater и подключаем диспетчер
    updater = Updater(token=BOT_TOKEN)

    # Добавляем обработчики команд
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Запускаем бота
    print("Бот запущен...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
