# Day 24 - List Functions

numbers = [1, 2, 3, 4]

print("Original list:", numbers)

# append()
numbers.append(5)
print("After append:", numbers)

# insert()
numbers.insert(1, 10)
print("After insert:", numbers)

# extend()
numbers.extend([6, 7])
print("After extend:", numbers)

# pop()
numbers.pop()
print("After pop:", numbers)

# remove()
numbers.remove(10)
print("After remove:", numbers)

# del
del numbers[0]
print("After del:", numbers)

# clear()
numbers.clear()
print("After clear:", numbers)
