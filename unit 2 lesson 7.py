import telebot #импортируем библиотеку
bot = telebot.TeleBot(token='8012377575:AAEGhciG9u7icMEvx5zITW9lUImsIL7aP-w') #берем токен бота

@bot.message_handler(commands=['echo']) # проверка на команду эхо
def main(message): #ответ на эхо
    @bot.message_handler() #берем любое сообщение
    def info(message): #функция для ответа
        bot.reply_to(message, message.text) #ответ бота на сообщение пользователя