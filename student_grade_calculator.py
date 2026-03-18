# Student Grade Calculator

subjects = int(input("Enter number of subjects: "))
total = 0

for i in range(subjects):
    marks = int(input(f"Enter marks for subject {i+1}: "))
    total += marks

percentage = total / subjects

print("\nTotal Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A")
elif percentage >= 75:
    print("Grade: B")
elif percentage >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
