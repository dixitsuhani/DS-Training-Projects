# Accept a number and check whether it is a palindrome or not.

num = input("Enter a number to check whether it is a palindrome or not: ")
if(num == num[::-1]):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")