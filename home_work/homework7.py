import sqlite3


def create_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
        )
    """)

def insert_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
    INSERT INTO books 
    (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?, ?, ?, ?, ?, ?)""",
    (name, author, publication_year, genre, number_of_pages, number_of_copies))
    conn.commit()

def get_all_books(conn):
    result = conn.execute("""
    SELECT * FROM books
    """)
    return result.fetchall()

def get_books_by_author(conn, author):
    result = conn.execute("""
    SELECT * FROM books WHERE author = ?
    """, (author,))
    return result.fetchall()

def delete_books_by_id(conn, book_id):
    conn.execute("""
    DELETE FROM books WHERE id = ?
    """, (book_id,))
    conn.commit()

if __name__ == "__main__":
    connection = sqlite3.connect('MyBooks.db')
    create_table(connection)
    insert_books(connection, "Test", "Test", 2026, "Test", 100, 1)
    get_all_books(connection)
    get_books_by_author(connection, "Test")
    delete_books_by_id(connection, 1)
    connection.commit()
    print(get_all_books(connection))

    connection.close()