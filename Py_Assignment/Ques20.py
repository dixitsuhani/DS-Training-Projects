# Write a function that checks  if a string is a pangram.

def Pangram(sentence):
    sentence = sentence.lower()
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabets:
        if letter not in sentence:
            return False
    return True
string = input("Enter a sentence: ")
if Pangram(string):
    print("It is a pangram.")
else:
    print("It is not a pangram.")