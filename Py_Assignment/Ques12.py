# Create a program to convert Celsius to Fahrenheit.

temp = int(input("Enter the temperature (in Celsius): "))
fahrenheit = (temp * 9/5) + 32
degree_sym = chr(176)
print(f"{temp}{degree_sym}C = {fahrenheit}{degree_sym}F")