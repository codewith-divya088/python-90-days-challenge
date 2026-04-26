import sqlite3

conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course_id INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT
)
""")

# insert sample data
cursor.execute("INSERT INTO courses (course_name) VALUES ('CSE')")
cursor.execute("INSERT INTO courses (course_name) VALUES ('AI')")

cursor.execute("INSERT INTO students (name, course_id) VALUES ('Divya', 1)")
cursor.execute("INSERT INTO students (name, course_id) VALUES ('Anshu', 2)")

conn.commit()

# JOIN query
cursor.execute("""
SELECT students.name, courses.course_name
FROM students
JOIN courses ON students.course_id = courses.id
""")

rows = cursor.fetchall()

print("Student with Course:")
for row in rows:
    print(row)

conn.close()
