import sqlite3
import random


def get_book():
    no_book = random.randint(1, 30)

    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM books
    WHERE id = (?)
    """, (no_book,))

    book = cursor.fetchone()

    conn.commit()
    conn.close()

    return book
