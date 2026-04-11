class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")

# Create object
s1 = Student("Divya", "Python")

# Call method
s1.display()
