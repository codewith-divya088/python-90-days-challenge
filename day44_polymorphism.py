# Method Overloading (simulated using default arguments)
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print("Sum of 2 numbers:", calc.add(2, 3))
print("Sum of 3 numbers:", calc.add(2, 3, 4))


# Method Overriding
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):   # overriding parent method
        print("Dog barks")

class Cat(Animal):
    def sound(self):   # overriding parent method
        print("Cat meows")

# Using polymorphism
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
