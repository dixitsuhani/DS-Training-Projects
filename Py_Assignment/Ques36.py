# Use list comprehension to create a list of sqaures of even numbers from 1 to 20.

squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(squares)