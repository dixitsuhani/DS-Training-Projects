# Build a basic CLI app that takes user input and performs basic operations.

while(True):
    print("1. Add\t\t2. Subtract\t\t3. Exit")
    choice = input("Enter choice: ")
    if choice == "3":
        print("Exiting loop...")
        break

    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    if choice == "1":
        print("Result: ",a + b)
    elif choice == "2":
        print("Result: ",a - b)
    else:
        print("Invalid choice!")