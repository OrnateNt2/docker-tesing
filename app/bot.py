from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
import sqlite3

# Укажите путь к базе данных
DB_PATH = "/usr/src/app/data/database.db"

# Этапы для ConversationHandler
WAITING_FOR_INPUT = 1

# Функция для получения данных из базы
def get_data():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Функция для добавления данных в базу
def add_data(info: str):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO data (info) VALUES (?)", (info,))
    conn.commit()
    conn.close()

# Обработчик команды /start
def start(update: Update, context: CallbackContext):
    data = get_data()
    if data:
        response = "\n".join([f"{row[0]}: {row[1]}" for row in data])
    else:
        response = "Данных в базе пока нет."
    update.message.reply_text(response)

# Обработчик команды /add
def add_command(update: Update, context: CallbackContext):
    update.message.reply_text("Введите данные, которые хотите добавить:")
    return WAITING_FOR_INPUT

# Обработчик текстового ввода для добавления в базу
def handle_input(update: Update, context: CallbackContext):
    user_input = update.message.text
    add_data(user_input)
    update.message.reply_text(f"Данные '{user_input}' успешно добавлены в базу!")
    return ConversationHandler.END

# Обработчик для отмены ввода
def cancel(update: Update, context: CallbackContext):
    update.message.reply_text("Добавление данных отменено.")
    return ConversationHandler.END

def main():
    # Создаём Updater и регистрируем обработчики
    updater = Updater(token="5729193808:AAFfQaNQ_CXMslH7WpDgSP90_rYTfV0CIbc")
    dp = updater.dispatcher

    # ConversationHandler для команды /add
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("add", add_command)],
        states={
            WAITING_FOR_INPUT: [MessageHandler(Filters.text & ~Filters.command, handle_input)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # Добавляем обработчики
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(conv_handler)

    # Запускаем бота
    print("Бот запущен...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
