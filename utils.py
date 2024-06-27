from queries import get_book


def generate_normal_text():
    book = get_book()
    text = f"""📚Title: {book[1]}
-----------------------------------------------------
🖌Author:   {book[2]}
-----------------------------------------------------
📅Publication year:   {book[3]}
-----------------------------------------------------
📜Genre:   {book[4]}
-----------------------------------------------------
📝Description:   {book[5]}
"""
    photo = book[6]

    return text, photo

