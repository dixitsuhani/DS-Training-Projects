# Accept a list and sort it out without using the sort function.

List = []
elements = int(input("Enter the number of elements: "))
for i in range(elements):
    num = int(input(f"Enter the {i+1} element of the list: "))
    List.append(num)
print(List)
for i in range(len(List)):
    min_Index = i
    for j in range(i + 1, len(List)):
        if List[j] < List[min_Index]:
            min_Index = j
    List[i], List[min_Index] = List[min_Index], List[i]
print("Sorted List: ", List)