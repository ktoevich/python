import telebot  # импортируем библиотеку

bot = telebot.TeleBot(token='8012377575:AAEGhciG9u7icMEvx5zITW9lUImsIL7aP-w')  # вводим токен бота

@bot.message_handler(commands=['hello'])  # создаем команду старт
def main(message):  # функция для отправки смс
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name}')  # отправляем смс с именем пользователя

bot.polling(none_stop=True)  # бот не останавливается