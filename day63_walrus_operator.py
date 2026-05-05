# Day 63 - Walrus Operator in Python

# normal way
number = int(input("Enter a number: "))

while number > 0:
    print("You entered:", number)
    number = int(input("Enter a number: "))


print("\nUsing Walrus Operator:\n")

# using walrus operator
while (num := int(input("Enter a number: "))) > 0:
    print("You entered:", num)

print("Loop ended")
