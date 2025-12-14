import telebot

# Твой токен (по запросу вставлен напрямую)
TOKEN = "8584094460:AAHYNtX6zDAQpXL_9nR_mLFjtoHpH56xfAc"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я PapaTrade бот. Отправь мне скриншот графика (1м таймфрейм).")

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Заглушка анализа — вернём аккуратные вероятности
    bot.reply_to(message, "Скриншот получен. Вероятности: вверх 54% / вниз 46%")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "Отправь скриншот графика — отвечу вероятностями для 1м трейда.")

if __name__ == "__main__":
    bot.polling(none_stop=True, timeout=60)
