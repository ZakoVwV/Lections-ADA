import telebot
from decouple import config
from parser import *

token = config('TOKEN')

bot = telebot.TeleBot(token)

keyboard = telebot.types.InlineKeyboardMarkup()
btn1 = telebot.types.InlineKeyboardButton('Описание', callback_data='description')
btn2 = telebot.types.InlineKeyboardButton('Фото', callback_data='photo')
btn3 = telebot.types.InlineKeyboardButton('Выход', callback_data='quit')
keyboard.add(btn1, btn2, btn3)

num_of_new = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я новостной бот')
    # print(message) # вся информация о чате, сообщений итд

@bot.message_handler(content_types=['text'])
def list_news(message):
    bot.send_message(message.chat.id, get_list_news())
    msg = bot.send_message(message.chat.id, 'Выбери номер новости (1-20):')
    bot.register_next_step_handler(msg, new)

def new(message):
    global num_of_new
    num_of_new = int(message.text)
    bot.send_message(message.chat.id, 'Выбери фото или описание какой либо новости:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda x: True)
def get_discription_or_photo(x):
    chat_id = x.message.chat.id
    if x.data == 'description':
        bot.send_message(chat_id, get_one_new(num_of_new))
    elif x.data == 'photo':
        bot.send_message(chat_id, get_photo(num_of_new))
    elif x.data == 'quit':
        bot.send_message(chat_id, 'До свидания')

bot.polling()