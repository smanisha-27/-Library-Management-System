class Book:
    def __init__(self, title):
        self.title = title
        self.__status = "Available"      
# Encapsulation

    def borrow(self):
        if self.__status == "Available":
            self.__status = "Borrowed"
            print("Book Borrowed")
        else:
            print("Book Not Available")

    def return_book(self):
        self.__status = "Available"
        print("Book Returned")

    def display(self):
        print("Book:", self.title)
        print("Status:", self.__status)


# Inheritance
class Member(Book):
    def search_book(self):
        print("Searching Book:", self.title)


# Composition
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(book.title, "Added to Library")

    def show_books(self):
        print("\nLibrary Books:")
        for b in self.books:
            print("-", b.title)


# Main Program
library = Library()

book1 = Member("Python Programming")
book2 = Member("Data Science")

library.add_book(book1)
library.add_book(book2)

library.show_books()

book1.search_book()
book1.borrow()
book1.display()
book1.return_book()
book1.display()"""
