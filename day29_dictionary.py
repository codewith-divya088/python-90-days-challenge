# Day 29 - Dictionary in Python

# Creating a dictionary
student = {
    "name": "Divya",
    "age": 20,
    "course": "B.Tech"
}

# Accessing values
print("Name:", student["name"])

# Adding a new key-value pair
student["marks"] = 85
print("After adding marks:", student)

# Updating value
student["age"] = 21
print("After updating age:", student)

# Removing a key
student.pop("course")
print("After removing course:", student)

# Loop through dictionary
print("All key-value pairs:")
for key, value in student.items():
    print(key, ":", value)
