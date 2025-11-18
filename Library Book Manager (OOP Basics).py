# 🔥 Beginner OOP Python Project of the Day

# Project: Library Book Manager (OOP Basics)

# 🎯 Goal
# Create a simple system to manage books in a library using classes and objects.

# 🧩 Requirements
# 1. Class: Book

# Each book should have:
# title
# author
# year
# available (True/False, default True)

# Methods:
# display_info(self) → print book details
# borrow_book(self) → if available, mark as not available
# return_book(self) → mark as available

# 2. Main Program
# Create an empty list library = []

# Menu:
# --- Library Manager ---
# 1. Add Book
# 2. View All Books
# 3. Borrow Book
# 4. Return Book
# 5. Quit


# Add Book → ask for title, author, year → create Book object → append to library list
# View All Books → loop through library → call display_info()
# Borrow/Return Book → ask for title → find the book in the list → call borrow_book() / return_book()

# 3. Exit
# Gracefully end the program when user selects Quit.

class Book:
    def __init__(self, title, author, year, available = True):
        self.title = title
        self.author = author
        self.year = year
        self.available = available
    
    def display_info(self):
        print(f"Title: {self.title} | Author: {self.author} | Year: {self.year} | Available: {self.available}")
    
    def borrow_book(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}'")
        else:
            print(f"'{self.title}' is already borrowed.")           
    
    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}'")
        else:
            print(f"'{self.title}' was not borrowed.")

bookList = []

def add_book():
    global bookList
    title = input("Enter the title of the book: ").lower()
    author = input("Enter the author of the book: ")
    year = int(input("Enter the year the book was published: "))
    return Book(title, author, year)


def view_all_books():
    global bookList
    for books in bookList:
        books.display_info()


def borrow_book():
    global bookList
    title = input("Enter the name of the book you want to borrow: ").lower()
    for books in bookList:
        if title.lower() == books.title:#Comparing the title entered by user to the book title in object
            books.borrow_book()
            return #Stops function after the book is found
    print("Book not found in library")#This ruins if the loop exits without finding anything

def return_book():
    global bookList
    title = input("Enter the name of the book you want to return: ").lower()
    for books in bookList:
        if title.lower() == books.title:
            books.return_book()
            return #Stops the whole function after borrowing
    print("Book not found in library")#This ruins if the loop exits without finding anything


while True:
    options = input("\n--- Library Manager ---\n1. Add Book\n2. View All Books\n3. Borrow Book\n4. Return Book\n5. Quit\n\nChoose an option >>> ")
    try:
        options = int(options)
        if options < 1 or options > 5:
            print("Please enter a valid option")
        else:
            if options == 1:
                book = add_book()
                bookList.append(book)
            elif(options == 2):
                view_all_books()
            elif(options == 3):
                borrow_book()
            elif(options == 4):
                return_book()
            elif(options == 5):
                print("Goodbye!")
                break
    except ValueError as V:
        print(f"Invalid Option {V}")