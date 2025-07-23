# Find the second largest number in the list.

List= []
List = []
elements = int(input("Enter the number of elements: "))
for i in range(elements):
    num = int(input(f"Enter the {i+1} element of the list: "))
    List.append(num)
print(List)
List.remove(max(List))
print("The second largest item of the list is: ", max(List))