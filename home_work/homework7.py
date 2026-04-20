def create_table(conn):
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books(
    name TEXT,
    author TEXT,
    publition_year INTEGER,
    genre TEXT,
    number_of_pages INTEGER,
    number_of_copies INTEGER
    )
""")

def insert_books(conn, name, author, publition_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
INSERT INTO books 
VALUES (?, ?, ?, ?, ?, ?)""",
(name, author, publition_year, genre, number_of_pages, number_of_copies))
    conn.commit()

def get_all_books(conn):
    result = conn.execute("""
    SELECT * FROM books
""")
    return result.fetchall()