# Write a program to implement a simple calculator using functions.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y!=0:
        return x/y
    else:
        return "Cannot divide by 0!"
    
def calculator():
    print("Perform the basic claculations!!!")
    a= int(input("Enter the first number: "))
    b= int(input("Enter the second number: "))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice= int(input("Enter the operation you want to perform: "))

    if choice == 1:
        sum = add(a, b)
        print(f"{a} + {b} = {sum}")
    elif choice == 2:
        difference = subtract(a, b)
        print(f"{a} - {b} = {difference}")
    elif choice == 3:
        product = multiplication(a, b)
        print(f"{a} * {b} = {product}")
    elif choice == 4:
        result = division(a, b)
        print(f"{a} / {b} = {result}")
    else:
        print("Invalid operator...")

calculator()