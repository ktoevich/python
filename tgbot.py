import telebot
import webbrowser
bot = telebot.TeleBot(token='8012377575:AAEGhciG9u7icMEvx5zITW9lUImsIL7aP-w-d')

@bot.message_handler(commands = ['site', 'website'])
def site(message):
    webbrowser.open('https://itproger.com')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name} {message.from_user.last_name}')
    
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode='html')
    
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hi, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    
    
bot.polling(none_stop = True)