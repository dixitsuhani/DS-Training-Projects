# Write a program to find the factorial of a number using loop.

num = int(input("Enter a number: "))
k = num
if num == 0:
    print("Factorial of 0 is 0.")
else:
    for i in range(1 , num):
        num = num * i
print(f"Factorial of {k} is {num}.")