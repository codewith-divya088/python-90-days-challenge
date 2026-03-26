#List functions

l=[10,20,30,10,10,50]

c=l.count(10)
print(c)

# Day 25 - List Functions Practice

numbers = [10, 20, 30, 20, 40]

print("Original list:", numbers)

# count()
print("Count of 20:", numbers.count(20))

# max() and min()
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# index()
print("Index of 30:", numbers.index(30))

# sort()
numbers.sort()
print("Sorted list:", numbers)

# reverse()
numbers.reverse()
print("Reversed list:", numbers)
