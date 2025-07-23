# Create a simple login system using dictionary and input.

users = {"admin": "1234", "user": "pass"}

username = input("Enter the username: ")
password = input("Enter the password: ")

if users.get(username) == password:
    print("Login successful!")
else:
    print("Invalid username or password!")