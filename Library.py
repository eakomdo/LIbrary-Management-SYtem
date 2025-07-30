
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

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f'Book "{title}" by {author} added.')

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f'Book "{title}" removed.')
                return
        print(f'Book "{title}" not found.')

    def search_books(self, keyword):
        found = False
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(book)
                found = True
        if not found:
            print(f'No books found for "{keyword}".')


def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Display all books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Search for a book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)
        elif choice == '3':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)
        elif choice == '4':
            keyword = input("Enter a keyword to search: ")
            library.search_books(keyword)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
