# Accept a string an dcheck if it is an anagram of another.

def anagram(str1, str2):
    str1= str1.replace(" ", "").lower()
    str2= str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
a= input("Enter first string: ")
b= input("Enter second string: ")
if anagram(a, b):
    print("The strings are anagram.")
else:
    print("The strings are not anagrams.")