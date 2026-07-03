# Library Management System
# A simple beginner-level project using Classes, Objects,
# Inheritance, and Encapsulation


# ---------------------------
# 1. BOOK CLASS
# ---------------------------
class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.__isbn = isbn          # private attribute (encapsulation)
        self.available = available

    # getter for isbn
    def get_isbn(self):
        return self.__isbn

    # setter for isbn
    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn

    def display_info(self):
        status = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.__isbn}")
        print(f"Status: {status}")
        print("-" * 30)


# ---------------------------
# 2. MEMBER CLASS
# ---------------------------
class Member:
    def __init__(self, name, membership_id):
        self.name = name
        self.__membership_id = membership_id   # private attribute
        self.borrowed_books = []

    # getter for membership_id
    def get_membership_id(self):
        return self.__membership_id

    # setter for membership_id
    def set_membership_id(self, new_id):
        self.__membership_id = new_id

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is not available right now.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")


# ---------------------------
# 3. STAFF MEMBER CLASS (Inheritance)
# ---------------------------
class StaffMember(Member):
    def __init__(self, name, membership_id, staff_id):
        # call the parent class constructor
        super().__init__(name, membership_id)
        self.staff_id = staff_id

    def add_book(self, library, book):
        library.add_book(book)
        print(f"Staff member {self.name} added the book '{book.title}' to the library.")


# ---------------------------
# 4. LIBRARY CLASS
# ---------------------------
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_all_books(self):
        print("=== Library Book List ===")
        for book in self.books:
            book.display_info()


# ---------------------------
# 5. TESTING THE SYSTEM
# ---------------------------
if __name__ == "__main__":
    # create a library
    my_library = Library()

    # create some books
    book1 = Book("The Alchemist", "Paulo Coelho", "12345")
    book2 = Book("1984", "George Orwell", "67890")

    # add books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)

    # create a regular member
    member1 = Member("Rania", "M001")

    # create a staff member
    staff1 = StaffMember("Ahmed", "S001", "ST100")

    # staff adds a new book
    book3 = Book("Harry Potter", "J.K. Rowling", "11111")
    staff1.add_book(my_library, book3)

    # show all books
    my_library.show_all_books()

    # member borrows a book
    member1.borrow_book(book1)

    # try to borrow the same book again with another member
    member2 = Member("Sara", "M002")
    member2.borrow_book(book1)

    # member returns the book
    member1.return_book(book1)

    # show updated book list
    my_library.show_all_books()

    # using getters and setters
    print("Book1 ISBN (using getter):", book1.get_isbn())
    book1.set_isbn("99999")
    print("Book1 new ISBN:", book1.get_isbn())

    print("Member1 ID (using getter):", member1.get_membership_id())