# Day 57 - HackerRank Practice (Basic Python)

# 1. Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Find maximum of 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Max number is:", max(a, b, c))


# 3. Sum of numbers from 1 to n
n = int(input("Enter n: "))
sum_n = 0

for i in range(1, n + 1):
    sum_n += i

print("Sum:", sum_n)


# 4. Reverse a string
text = input("Enter a string: ")
print("Reversed:", text[::-1])


# 5. Count vowels
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowel count:", count)
