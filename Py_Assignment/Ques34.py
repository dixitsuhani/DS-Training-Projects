# Implement a generator to yield even numbers from 1 to n.

def EvenNo_Gen(n):
    for i in range (2, n+1, 2):
        yield i
n_input= int(input("Enter the value of n: "))
for a in EvenNo_Gen(n_input):
    print(a)