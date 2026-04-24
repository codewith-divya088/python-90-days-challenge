import sqlite3


def connect_db():
    return sqlite3.connect("student.db")


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    )
    """)
    conn.commit()


def add_student(conn):
    name = input("Enter name: ")
    age = int(input("Enter age: "))

    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("✅ Student added")


def view_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n📋 Student Records:")
    for row in rows:
        print(row)


def update_student(conn):
    student_id = int(input("Enter ID to update: "))
    new_name = input("Enter new name: ")
    new_age = int(input("Enter new age: "))

    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET name = ?, age = ? WHERE id = ?",
        (new_name, new_age, student_id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ No record found")
    else:
        print("✏️ Record updated successfully")


def delete_student(conn):
    student_id = int(input("Enter ID to delete: "))

    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ No record found")
    else:
        print("🗑️ Record deleted successfully")


def main():
    conn = connect_db()
    create_table(conn)

    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(conn)
        elif choice == "2":
            view_students(conn)
        elif choice == "3":
            update_student(conn)
        elif choice == "4":
            delete_student(conn)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()
