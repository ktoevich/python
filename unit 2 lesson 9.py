import telebot  # импортируем библиотеку

bot = telebot.TeleBot(token='8012377575:AAEGhciG9u7icMEvx5zITW9lUImsIL7aP-w')  # вводим токен бота

# Никогда не пиши хардкод: никогда не храни пароли и токены в коде
# Лучше храни их в переменных окружения или в отдельных файлах, которые не загружаются в репозиторий на пример .env или .env.local
# А другим разработчикам примеры ключей (не настоящие) можешь оставить в .env.example

@bot.message_handler(commands=['hello'])  # создаем команду старт
def main(message):  # функция для отправки смс
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name}')  # отправляем смс с именем пользователя

bot.polling(none_stop=True)  # бот не останавливается