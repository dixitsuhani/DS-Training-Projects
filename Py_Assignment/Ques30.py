# Create a Python program using OOP for student management (class, object, init).

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}, Roll No.: {self.roll_no}")

s1 = Student("Suhani", 44)
s1.display() 