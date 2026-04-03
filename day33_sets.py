# Day 33 - Sets in Python

# Creating a set
numbers = {1, 2, 3, 4, 4, 5}
print("Set:", numbers)  # duplicates removed

# add()
numbers.add(6)
print("After add:", numbers)

# remove()
numbers.remove(2)
print("After remove:", numbers)

# union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1.union(set2))

# intersection()
print("Intersection:", set1.intersection(set2))

# difference()
print("Difference:", set1.difference(set2))
