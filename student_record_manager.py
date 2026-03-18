students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        if marks >= 40:
            result = "Pass"
        else:
            result = "Fail"

        students.append((name, marks, result))
        print("Student added successfully!")

    elif choice == "2":
        print("\n--- Student Records ---")
        for s in students:
            print(f"Name: {s[0]}, Marks: {s[1]}, Result: {s[2]}")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
