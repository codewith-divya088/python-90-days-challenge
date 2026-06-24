# Day 69 - Library Management System
# Practicing Dictionaries in Python

# Dictionary to store books
library = {}


# Function to add a new book
def add_book():

    book_id = int(input("Enter Book ID: "))
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")

    library[book_id] = {
        "title": title,
        "author": author
    }

    print("Book Added Successfully!")


# Function to view all books
def view_books():

    if len(library) == 0:
        print("No Books Available.")
        return

    print("\nLibrary Books:")

    for book_id, details in library.items():

        print("\nBook ID:", book_id)
        print("Title:", details["title"])
        print("Author:", details["author"])


# Function to search a book
def search_book():

    book_id = int(input("Enter Book ID to Search: "))

    if book_id in library:

        print("\nBook Found")
        print("Title :", library[book_id]["title"])
        print("Author:", library[book_id]["author"])

    else:
        print("Book Not Found.")


# Function to delete a book
def delete_book():

    book_id = int(input("Enter Book ID to Delete: "))

    if book_id in library:

        del library[book_id]

        print("Book Deleted Successfully!")

    else:
        print("Book Not Found.")


# Main Menu
while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Delete Book")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_book()

    elif choice == 2:
        view_books()

    elif choice == 3:
        search_book()

    elif choice == 4:
        delete_book()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice. Please Try Again.")
