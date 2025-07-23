# Accept a list of numbers and return the average.

List = []
elements = int(input("Enter the number of elements: "))
for i in range(elements):
    num = int(input(f"Enter the {i+1} element of the list: "))
    List.append(num)
print(List)
print("Average of the list is: ", sum(List)/elements)