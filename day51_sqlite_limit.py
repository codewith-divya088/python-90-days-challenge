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


def insert_students(conn):
    cursor = conn.cursor()

    data = [
        ("Divya", 20),
        ("Anshu", 18),
        ("Rahul", 22),
        ("Neha", 21),
        ("Amit", 23)
    ]

    cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", data)
    conn.commit()
    print("✅ Multiple records inserted")


def fetch_limited_data(conn, limit):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students LIMIT ?", (limit,))
    rows = cursor.fetchall()

    print(f"\n📋 Showing {limit} records:")
    for row in rows:
        print(row)


def main():
    conn = connect_db()
    create_table(conn)

    insert_students(conn)

    limit = int(input("Enter how many records to display: "))
    fetch_limited_data(conn, limit)

    conn.close()


if __name__ == "__main__":
    main()
