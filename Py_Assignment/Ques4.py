# Write a program to count the number of vowels in a string.

string= input("Enter a string: ")
Vowel= "AaEeIiOoUu"
i = 0
for a in string:
    if a in Vowel:
        i = i+1
print(f"{string} has {i} vowels.")