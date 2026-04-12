class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):  # Inheriting from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()
