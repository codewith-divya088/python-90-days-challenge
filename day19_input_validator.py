# Day 19: Input Validator

user_input = input("Enter something: ")

if user_input.isalpha():
    print("You entered only alphabets")

elif user_input.isdigit():
    print("You entered only numbers")

elif user_input.isalnum():
    print("You entered alphabets and numbers")

else:
    print("You entered special characters")
