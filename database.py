import json

import sqlite3

with open('book_info.json', mode='r', encoding='utf-8') as file:
    data = json.load(file)

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

for book in data:
    id = book['id']
    title = book['title']
    author = book['author']
    publication_year = book['publication_year']
    genre = book['genre']
    description = book['description']
    cover_image = book['cover_image']

    cursor.execute('''
        INSERT INTO books (id, title, author, publication_year, genre, 
        description, cover_image)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (id, title, author, publication_year, genre,
          description, cover_image))


conn.commit()
conn.close()
