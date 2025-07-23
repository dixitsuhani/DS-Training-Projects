# Create a calculator using if-else.

A= int(input("Enter first number: "))
B= int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit the loop")

while(True):
    Choice = int(input("Enter your choice: "))
    if Choice==1:
        print(f"The addition of {A} and {B} is: ", A + B)
    elif Choice==2:
        print(f"The difference between {A} and {B} is: ", A - B)
    elif Choice==3:
        print(f"The product of {A} and {B} is: ", A * B)
    elif Choice==4:
        print(f"{A} divided by {B} is: ", A / B)
    elif Choice==5:
        print("Exiting the loop...")
        break
    else:
        print("Invalid operator!")