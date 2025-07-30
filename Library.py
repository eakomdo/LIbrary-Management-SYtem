
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

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.status == "available":
                    book.status = "borrowed"
                    print(f'You have borrowed "{title}".')
                    return
                else:
                    print(f'Book "{title}" is already borrowed.')
                    return
        print(f'Book "{title}" not found.')

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.status == "borrowed":
                    book.status = "available"
                    print(f'You have returned "{title}".')
                    return
                else:
                    print(f'Book "{title}" was not borrowed.')
                    return
        print(f'Book "{title}" not found.')


def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Display all books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Search for a book")
        print("5. Borrow a book")
        print("6. Return a book")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            library.display_books()
        elif choice == '2':
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            if title and author:
                library.add_book(title, author)
            else:
                print("Both title and author are required.")
        elif choice == '3':
            title = input("Enter the title of the book to remove: ").strip()
            if title:
                library.remove_book(title)
            else:
                print("Title is required.")
        elif choice == '4':
            keyword = input("Enter a keyword to search: ").strip()
            if keyword:
                library.search_books(keyword)
            else:
                print("Keyword is required.")
        elif choice == '5':
            title = input("Enter the title of the book to borrow: ").strip()
            if title:
                library.borrow_book(title)
            else:
                print("Title is required.")
        elif choice == '6':
            title = input("Enter the title of the book to return: ").strip()
            if title:
                library.return_book(title)
            else:
                print("Title is required.")
        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
