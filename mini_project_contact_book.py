# Mini Project - Contact Book

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts[name] = number
        print("Contact added!")

    elif choice == "2":
        print("Contacts:", contacts)

    elif choice == "3":
        name = input("Enter name to search: ")
        print("Number:", contacts.get(name, "Not found"))

    elif choice == "4":
        name = input("Enter name to delete: ")
        contacts.pop(name, None)
        print("Deleted (if existed)")

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
