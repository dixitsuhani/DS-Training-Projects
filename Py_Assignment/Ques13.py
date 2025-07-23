# Write a python function to find the maximum of two numbers.

def Maximum(num1, num2):
    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}.")
    else:
        print("Both values are equal.")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
Maximum(a, b)