# Write a program to print the fibonacci series upto n terms.

num = int(input("Enter the number of terms: "))
a = 0
b = 1
for i in range(num):
    print(a, end = " ")
    a , b = b , a + b