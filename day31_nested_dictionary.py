# Day 31 - Nested Dictionary in Python

# Creating a nested dictionary
students = {
    "student1": {
        "name": "Divya",
        "age": 20,
        "marks": 85
    },
    "student2": {
        "name": "Anshu",
        "age": 15,
        "marks": 90
    }
}

# Accessing data
print("Student1 Name:", students["student1"]["name"])

# Adding new student
students["student3"] = {
    "name": "Riya",
    "age": 19,
    "marks": 88
}

print("After adding new student:", students)

# Loop through nested dictionary
for key, value in students.items():
    print(key, ":", value)
