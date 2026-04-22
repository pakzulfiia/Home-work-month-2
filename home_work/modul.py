import sqlite3
from homework7 import (create_table, insert_books, get_all_books, get_books_by_author, delete_books_by_id)


connection = sqlite3.connect('MyBooks.db')
create_table(connection)

insert_books(connection, "1984", "George Orwell", 1949, "Dystopian", 328, 12)
insert_books(connection, "To Kill a Mockingbird", "Harper Lee", 1960, "Fiction", 281, 8)
insert_books(connection, "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", 180, 10)
insert_books(connection, "War and Peace", "Leo Tolstoy", 1869, "Historical", 1225, 3)
insert_books(connection, "Moby-Dick", "Herman Melville", 1851, "Adventure", 635, 5)
insert_books(connection, "Pride and Prejudice", "Jane Austen", 1813, "Romance", 432, 7)
insert_books(connection, "The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction", 277, 9)
insert_books(connection, "The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 11)
insert_books(connection, "Crime and Punishment", "Fyodor Dostoevsky", 1866, "Philosophical", 671, 4)
insert_books(connection, "Brave New World", "Aldous Huxley", 1932, "Science Fiction", 311, 6)

authors_book = get_books_by_author(connection, 'Leo Tolstoy')
print(get_all_books(connection))
print()

del_book = delete_books_by_id(connection, 5)
print(get_all_books(connection))
print()

for b in get_all_books(connection):
    print(b)

connection.close()