import sqlite3

def create_connection():
    conn = sqlite3.connect("student.db")
    print("✅ Database connected successfully")
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
    print("✅ Table created successfully")


def insert_data(conn):
    cursor = conn.cursor()

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
                   (name, age, course))

    conn.commit()
    print("✅ Data inserted successfully")


def display_data(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n📋 Student Records:")
    for row in rows:
        print(row)


def main():
    conn = create_connection()
    create_table(conn)

    while True:
        print("\n1. Insert Data")
        print("2. View Data")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            insert_data(conn)
        elif choice == "2":
            display_data(conn)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice")

    conn.close()


if __name__ == "__main__":
    main()
