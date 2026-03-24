# Day 23 - List Comprehension

# Normal way using loop
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num * num)

print("Squares using loop:", squares)

# Using list comprehension
squares2 = [num * num for num in numbers]

print("Squares using list comprehension:", squares)

##Another examples 
l=[]
for a in range(1,101):
  l.append(a)
  print(l)
