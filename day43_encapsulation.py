class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks   # private variable

    # Getter
    def get_marks(self):
        return self.__marks

    # Setter
    def set_marks(self, marks):
        if marks >= 0:
            self.__marks = marks

s = Student("Divya", 90)

print(s.get_marks())

s.set_marks(95)
print(s.get_marks())
