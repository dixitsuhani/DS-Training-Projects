# Create a function that takes a list and returns only unique elements.

def unique_list(a):
    return list(set(a))
print(unique_list([1, 2, 4, 4, 2, 5, 6, 6]))