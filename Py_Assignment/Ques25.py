# Write a function to count uppercase and lowercase letters in a string.

def count(string):
    upper= 0
    lower= 0
    for char in string:
        if char.isupper():
            upper+=1
        else:
            lower+=1
    print("Uppercase letters: ", upper)
    print("Lowercase letters: ", lower)
text= input("Enter a text: ")
count(text)