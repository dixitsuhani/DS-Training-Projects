# Accept a list and print all elements greater than 50.

List = []
Above_50 = []
elements = int(input("Enter the number of elements: "))
for i in range(elements):
    num = int(input(f"Enter the {i+1} element of the list: "))
    List.append(num)
print(List)
for i in range(elements):
    if List[i] > 50:
        Above_50.append(List[i])
print("Elements greater than 50 are: ", Above_50)