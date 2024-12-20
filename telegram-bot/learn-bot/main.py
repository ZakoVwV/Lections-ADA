import telebot

from decouple import config


token = config('TOKEN')

bot = telebot.TeleBot(token)


"""
Декоратор message_handler нужен чтобы реагировать на определенные сообщения
Этот декоратор принимает commands - список команд (функция работает, когда пользователь написал одну из них)

content_types - список типов сообщения (text, audio, document, photo, sticker, video, video_note, voice, location, contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, pinned_message, web_app_data)

content_types=['text'] - функция будет работать, когда пользователь отправит в чат любое текстовое сообщение
content_types=['audio'] - функция будет работать, когда пользователь отправит аудио сообщение
"""

# клавиатура, которая находится так, где клавиатура
# keyboard = telebot.types.ReplyKeyboardMarkup()
# button1 = telebot.types.KeyboardButton('Да')
# button2 = telebot.types.KeyboardButton('Нет')
# keyboard.add(button1, button2)

"""
Клавиатура, которая будет прикрепится под сообщением
При нажатий на кнопку будет искаться функция, задекорированая callback_query_handler
"""
keyboard = telebot.types.InlineKeyboardMarkup()
button1 = telebot.types.InlineKeyboardButton('Да', callback_data='yes')
button2 = telebot.types.InlineKeyboardButton('Нет', callback_data='no')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(chat_id=message.chat.id, text='Привет, выбери кнопку!', reply_markup=keyboard)


# func - функция фильтр, в данном случае мы возвращаем True, пропуская все сообщения
@bot.callback_query_handler(func=lambda x: True)
def reply_to_button(call):
    if call.data == 'yes':
        bot.send_message(call.from_user.id,'Звезда')
    elif call.data == 'no':
        bot.send_message(call.from_user.id,'сам знаешь кого ответ')


    # register_next_step_handler() - принимает сообщение и функцию, которая вызывается как только пользователь отправит любое сообщение и передает в функциmessage_handlerю
#     bot.register_next_step_handler(message, reply_to_button)

# def reply_to_button(message):
#     if message.text == 'Да':
#         bot.send_message(message.chat.id, 'Звезда')
#     elif message.text == 'Нет':
#         bot.send_message(message.chat.id, 'Сам знаешь кого ответ')
#     else:
#         bot.send_message(message.chat.id, 'Нажми на кнопку!')
#         bot.register_next_step_handler(message, reply_to_button)



# @bot.message_handler(commands=['start', 'hello'])
# def start_message(message):
#     print(message)
#     bot.send_message(message.chat.id, 'Привет') # Отправит соощение привет в указанный чат (id чата берется из message, который принимает функция)

bot.polling()