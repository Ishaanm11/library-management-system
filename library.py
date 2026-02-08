from database import get_connection

class Library:

    def displayAvailableBooks(self):
        conn = get_connection()
        cursor = conn.cursor()

        print("\n--- AVAILABLE BOOKS ---")
        cursor.execute("SELECT name FROM books")
        books = cursor.fetchall()

        if not books:
            print("No books available.")
        else:
            for book in books:
                print("•", book[0])

        conn.close()
        input("\nPress Enter to continue...")

    def borrowBook(self, student_name, book_name):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM books WHERE name=?", (book_name,))
        book = cursor.fetchone()

        if book is None:
            print("\nBook not available.")
        else:
            cursor.execute(
                "INSERT INTO issued_books (student_name, book_name) VALUES (?, ?)",
                (student_name, book_name)
            )
            cursor.execute("DELETE FROM books WHERE name=?", (book_name,))
            conn.commit()
            print("\nBook issued successfully.")

        conn.close()

    def returnBook(self, book_name):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT book_name FROM issued_books WHERE book_name=?",
            (book_name,)
        )
        record = cursor.fetchone()

        if record is None:
            print("\nThis book was not issued.")
        else:
            cursor.execute(
                "DELETE FROM issued_books WHERE book_name=?",
                (book_name,)
            )
            cursor.execute(
                "INSERT INTO books (name) VALUES (?)",
                (book_name,)
            )
            conn.commit()
            print("\nBook returned successfully.")

        conn.close()

    def donateBook(self, book_name):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT OR IGNORE INTO books (name) VALUES (?)",
            (book_name,)
        )
        conn.commit()

        print("\nBook donated successfully.")
        conn.close()