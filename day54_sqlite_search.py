import sqlite3

# connect to database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
""")

# take input for search
name = input("Enter name to search: ")

# search query
cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
rows = cursor.fetchall()

print("\nSearch Results:")
if len(rows) == 0:
    print("No record found")
else:
    for row in rows:
        print(row)

conn.close()
