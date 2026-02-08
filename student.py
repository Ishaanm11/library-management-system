class Student:

    def requestBook(self):
        return input("Enter book name to borrow: ").strip()

    def returnBook(self):
        return input("Enter book name to return: ").strip()

    def donateBook(self):
        return input("Enter book name to donate: ").strip()