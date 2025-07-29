
# Book class represents a single book in the library
class Book:
    def __init__(self, title, author, status="available"):
        self.title = title
        self.author = author
        self.status = status  # 'available' or 'borrowed'

    def __str__(self):
        return f"{self.title} by {self.author} [{self.status}]"


# Library class manages a collection of books
class Library:
    def __init__(self):
        self.books = []  # List to store Book objects

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")
