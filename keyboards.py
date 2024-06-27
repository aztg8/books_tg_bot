from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def generate_get_book_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    get_book_btn = KeyboardButton(text="Получить книгу📕")

    markup.add(get_book_btn)

    return markup
