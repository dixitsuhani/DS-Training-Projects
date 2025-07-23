# Write a python program using a lambda function to square all elements in a list.

num_list= [1, 2, 3, 4, 5]
squares= list(map(lambda x: x**2, num_list))
print("Squares of numbers in the list: ", squares)