# Demonstrate the use of map(), filter() and reduce() on a list.

from functools import reduce
a = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, a))
even = list(filter(lambda x: x % 2 == 0, a))
sum = reduce(lambda x, y: x + y, a)

print("Squared Values: ", squared)
print("Even Values: ", even)
print("Sum: ", sum)