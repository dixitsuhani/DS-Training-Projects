# Create a function that returns a list of prime numbers from 1 to 100.

def Prime():
    prime = []
    for num in range(2, 101):
        for i in range(2, 11):
            if num % i == 0:
                break
        else:
            prime.append(num)
    return prime
print(Prime())