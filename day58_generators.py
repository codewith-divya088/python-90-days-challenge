# Day 58 - Generators in Python

# simple generator function
def numbers():
    for i in range(1, 6):
        yield i

# using generator
gen = numbers()

print("Generator Output:")

for value in gen:
    print(value)


# generator for square numbers
def square_numbers(n):
    for i in range(1, n + 1):
        yield i * i

print("\nSquare Numbers:")

for num in square_numbers(5):
    print(num)
