# Implement a program to demonstrate try-except-finally for exception handling.

try:
    a = int(input("Enter a number: "))
    print(100 / a)
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This runs no matter what.")