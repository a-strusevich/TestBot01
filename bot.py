import telebot;

bot = telebot.TeleBot('6595393373:AAGeP42CJc4yqI4_mpxzP1PEkbVxxXVDLVY');

# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     bot.send_message(message.from_user.id, 'Привет!')
# @bot.message_handler(commands=['stop'])
# def handle_stop(message):
#     bot.send_message(message.from_user.id, 'Бот останавливается...')
# # Выполнение завершающих операций
# # Сохранение данных
# # Закрытие соединений
#     bot.stop()
#     bot.polling(none_stop=True)
#


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Юзера ответ")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
