# Example of Exception Handling

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    result = a / b

except ValueError:
    print("Please enter valid numbers")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program executed successfully")
