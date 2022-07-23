from .database_connection import DataBaseConnection
import sqlite3
books = 'books_data.txt'

def create_database():
    with DataBaseConnection('data.db') as connection:
        cursor= connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read int)')

def add_book(name,author):
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?,?,0)',(name,author))

def print_info():
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM books')
        books =[{'book': line[0],
                    'author': line[1],
                    'read': line[2]} for line in cursor.fetchall()]


    return books
def listing():
    books  = print_info()
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"""
        Book   : {book['book']},
        Author : {book['author']},
        Read   : {read}""")

def searching(name):
    books = print_info()
    for book in books:
        if name == book['book']:
            read = 'Yes' if book['read'] else 'No'
            print(f"""
                    Book   : {book['book']},
                    Author : {book['author']},
                    Read   : {read}""")
            break
    else:
        print("Book doesn't exist -_-")


def deleting(name):
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books where name=?', (name,))

def mark(name):
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

def _smash():
    with DataBaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE  FROM books')
