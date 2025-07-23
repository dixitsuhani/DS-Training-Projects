# Display the multiplication table of a given number.

num = int(input("Enter a number: "))
i = 1
for i in range(1, 11):
    b = num * i
    print(f"{num} x {i} = {b}")
    i = i + 1