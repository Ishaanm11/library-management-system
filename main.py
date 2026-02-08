from library import Library
from student import Student
from database import setup_database, get_connection

def preload_books():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM books")
    if cursor.fetchone()[0] == 0:
        books = [
            "vistas",
            "invention",
            "rich&poor",
            "indian",
            "macroeconomics",
            "microeconomics"
        ]
        for book in books:
            cursor.execute("INSERT INTO books (name) VALUES (?)", (book,))
        print("Sample books added.\n")

    conn.commit()
    conn.close()

if __name__ == "__main__":

    setup_database()
    preload_books()

    library = Library()
    student = Student()

    while True:
        print("""
====== LUCKNOW LIBRARY ======
1. List all books
2. Borrow book
3. Return book
4. Donate book
5. Track issued books
6. Exit
""")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                library.displayAvailableBooks()

            elif choice == 2:
                name = input("Enter your name: ")
                library.borrowBook(name, student.requestBook())

            elif choice == 3:
                library.returnBook(student.returnBook())

            elif choice == 4:
                library.donateBook(student.donateBook())

            elif choice == 5:
                conn = get_connection()
                cursor = conn.cursor()

                print("\n--- ISSUED BOOKS ---")
                cursor.execute("SELECT student_name, book_name FROM issued_books")
                records = cursor.fetchall()

                if not records:
                    print("No books are issued.")
                else:
                    for s, b in records:
                        print(f"{b} → {s}")

                conn.close()
                input("\nPress Enter to continue...")

            elif choice == 6:
                print("Thank you. Visit again!")
                break

            else:
                print("Invalid option.")

        except ValueError:
            print("Please enter a number.")