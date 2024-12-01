import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Укажите токен вашего бота
BOT_TOKEN = "5729193808:AAFfQaNQ_CXMslH7WpDgSP90_rYTfV0CIbc"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Функция для получения данных из SQLite
def get_data():
    conn = sqlite3.connect("app/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Команда /start
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    data = get_data()
    if data:
        response = "\n".join([f"{row[0]}: {row[1]}" for row in data])
    else:
        response = "Данных в базе пока нет."
    await message.reply(response)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
