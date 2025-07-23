# Write a function to check if the input is number or not.

def is_Num (a):
    try:
        float(a)
        return True
    except ValueError:
        return False
user_input = input("Enter something: ")

if is_Num(user_input):
    print("It is a number.")
else:
    print("It is not a number.")