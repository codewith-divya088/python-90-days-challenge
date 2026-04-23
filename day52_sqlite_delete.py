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


def insert_student(conn, name, age):
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


def delete_student(conn, student_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ No record found with that ID")
    else:
        print("🗑️ Record deleted successfully")


def main():
    conn = connect_db()
    create_table(conn)

    while True:
        print("\n--- Menu ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            insert_student(conn, name, age)

        elif choice == "2":
            view_students(conn)

        elif choice == "3":
            student_id = int(input("Enter ID to delete: "))
            delete_student(conn, student_id)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()
