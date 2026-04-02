# Day 32 - Tuple in Python

# Creating a tuple
numbers = (10, 20, 30, 40)

print("Tuple:", numbers)

# Accessing elements
print("First element:", numbers[0])

# Length of tuple
print("Length:", len(numbers))

# Loop through tuple
for num in numbers:
    print(num)

# Tuple with different data types
mixed = (1, "Divya", 3.5)
print("Mixed tuple:", mixed)

# Trying to change value (will give error)
# numbers[0] = 100  # Tuples are immutable
