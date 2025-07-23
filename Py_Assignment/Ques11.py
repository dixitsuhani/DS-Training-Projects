# Find the sum of digits of a number using a while loop.

num = int(input("Enter a number to find the sum of digits: "))
k = num
Sum = 0
while num > 0:
    l = num % 10
    Sum = l + Sum
    num = num // 10
print(f"Sum of {k}= {Sum}")