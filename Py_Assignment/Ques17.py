# Accept a list and remove all duplicates from it.

Sent = input("Enter a sentence: ")
words = Sent.split()
F_List = list(set(words))
print(F_List)