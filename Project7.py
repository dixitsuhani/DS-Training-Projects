#login
username = "Suhani"
password = 30042006
a = 0
print("Welcome to Website !!!!!\n Please Login")

for i in range(3):
    print(f"You have Got {3 - i} Tries !!")
    user = input("Enter Your Username :")
    Pw = int(input("Enter Your Password :"))
    if (username == user and password == Pw):
        a = 1
        break
    elif (user != username and Pw != password):
        print("worrng password")
if a == 1:
    print("Login Successfull")
else :
    print("You are Out of tries !")