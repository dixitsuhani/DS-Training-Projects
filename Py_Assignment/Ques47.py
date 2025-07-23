# Write a function to flatten a nested list using recursion.

def flatten(abc):
    result = []
    for i in abc:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
print(flatten([1, [2, [3, 4]], 5]))