# Day 30 - Dictionary Functions in Python

student = {
    "name": "Divya",
    "age": 20,
    "course": "B.Tech"
}

# keys()
print("Keys:", student.keys())

# values()
print("Values:", student.values())

# items()
print("Items:", student.items())

# get()
print("Name:", student.get("name"))

# update()
student.update({"marks": 90})
print("After update:", student)

# pop()
student.pop("age")
print("After pop:", student)
