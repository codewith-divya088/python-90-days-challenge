# Student Result Calculator
# Day 66 - Practicing Functions

# Function to calculate total marks
def calculate_total(maths, science, english):
    total_marks = maths + science + english
    return total_marks


# Function to calculate percentage
def calculate_percentage(total):
    percentage = total / 3
    return percentage


# Function to assign grade
def get_grade(percentage):

    if percentage >= 90:
        return "A"

    elif percentage >= 75:
        return "B"

    elif percentage >= 60:
        return "C"

    else:
        return "D"


# Taking input from user
student_name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

# Calling functions
total = calculate_total(maths, science, english)
percentage = calculate_percentage(total)
grade = get_grade(percentage)

# Displaying result
print("\n----- Result -----")
print("Student Name :", student_name)
print("Total Marks  :", total)
print("Percentage   :", percentage)
print("Grade        :", grade)
