# Write a program to create a dictionary from two lists.

keys = ['Name', 'Age', 'City']
values = ['Suhani', 20, 'Delhi']

result_dict = dict(zip(keys, values))

print("The created dictionary is:")
print(result_dict)