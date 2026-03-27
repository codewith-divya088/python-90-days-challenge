# Day 26 - zip() function

names = ["Divya", "Anshu", "Riya"]
marks = [85, 90, 78]

# Using zip
combined = zip(names, marks)

# Convert to list to see output
result = list(combined)

print("Combined data:", result)

# Using loop
for name, mark in zip(names, marks):
    print(name, "scored", mark)
