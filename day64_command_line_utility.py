# Day 64 - Command Line Utility in Python

import sys

# checking command line arguments
if len(sys.argv) < 3:
    print("Usage: python day64_command_line_utility.py num1 num2")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)
    print("Division:", num1 / num2)
