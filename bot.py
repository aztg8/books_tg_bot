from telebot import TeleBot

from configs import TOKEN

from keyboards import *

from utils import *

bot = TeleBot(token=TOKEN)


@bot.message_handler(commands=['start'])
def cmd_start(message):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     f"""Привет!👋🏻""")
    ask_user_name(message)


@bot.message_handler(commands=['help'])
def cmd_help(message):
    chat_id = message.chat.id

    bot.send_message(chat_id,
                     f"""Я бот, который поможет вам выбрать книгу😊                    
Вам надо нажать на кнопку 'Книги📕'""")


def ask_user_name(message):
    chat_id = message.chat.id

    send_msg = bot.send_message(chat_id,
                                f"""Как к вам обращаться?""")

    bot.register_next_step_handler(send_msg, greeting_user)


def greeting_user(message):
    chat_id = message.chat.id
    name = message.text
    bot.send_message(chat_id,
                     f"""{name}, добро пожаловать в мир книг!
---------------------------------------------------------------------                     
Чтобы получить книгу нажмите на кнопку 'Получить книгу📕'""",
                     reply_markup=generate_get_book_button())


@bot.message_handler(func=lambda message: message.text == "Получить книгу📕")
def send_book(message):
    chat_id = message.chat.id
    data = generate_normal_text()

    bot.send_photo(chat_id,
                   photo=data[1],
                   caption=data[0])


bot.polling(none_stop=True)
