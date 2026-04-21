import sqlite3


def connect_db():
    conn = sqlite3.connect("student.db")
    return conn


def create_table(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
    """)

    conn.commit()


def insert_student(conn, name, age, course):
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    conn.commit()
    print("Student added successfully!")


def view_students(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n📋 Student Records:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")


def main():
    conn = connect_db()
    create_table(conn)

    while True:
        print("\n--- Student Database Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            course = input("Enter course: ")
            insert_student(conn, name, age, course)

        elif choice == "2":
            view_students(conn)

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()
