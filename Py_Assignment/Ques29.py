# Implement a recursive function to compute factorial.

def factorial(a):
    if a == 0 or a == 1:
        return 1
    return a * factorial(a - 1)
num = int(input("Enter a number: "))
print(factorial(num))