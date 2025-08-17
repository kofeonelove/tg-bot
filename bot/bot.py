import os
import dotenv
dotenv.load_dotenv()
import telebot
token=os.getenv('TOKEN')

bot=telebot.TeleBot(token=token)
@bot.message_handler(commands=['start'])
def start(message):
    markup=telebot.types.InlineKeyboardMarkup()
    b1=telebot.types.InlineKeyboardButton(text='Buy vpn',url='youtube.com')
    b2=telebot.types.InlineKeyboardButton(text='My keys',url='vk.ru')
    markup.add(b1)
    markup.add(b2)
    bot.send_message(message.from_user.id, 'Selling vpn bot',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def text_messages(message):
    if message=='Buy vpn':
        bot.send_message(message.from_user.id,'In working!')
    if message=='My keys':
        bot.send_message(message.from_user.id,'In working(other)')
bot.polling(none_stop=True, interval=0)
