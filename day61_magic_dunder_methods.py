# Day 61 - Magic / Dunder Methods in Python

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # dunder method for string representation
    def __str__(self):
        return f"Student Name: {self.name}, Marks: {self.marks}"

    # dunder method for addition
    def __add__(self, other):
        return self.marks + other.marks


# objects
s1 = Student("Divya", 85)
s2 = Student("Rahul", 90)

# using __str__
print(s1)

# using __add__
print("Total Marks:", s1 + s2)
