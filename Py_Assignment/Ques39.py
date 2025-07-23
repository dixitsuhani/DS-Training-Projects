# Create a class that inherits from another class and overrides a method.

class Animal:
    def speak(self):
        print("Animal speaks.")

class Dog(Animal):
    def speak(self):
        print("Dog barks.")

d = Dog()
d.speak()