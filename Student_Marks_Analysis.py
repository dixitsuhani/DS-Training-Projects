import pandas as Pd
import matplotlib.pyplot as Mp
df= Pd.read_csv(r"C:\Users\Student\Desktop\marks.csv")

def mean():
    print("Mean: ",df['Marks'].mean())

def median():
    print("Median: ", df['Marks'].median())

def mode():
    print("Mode: ", df['Marks'].mode())

def variance():
    print("Variance: ", df['Marks'].var())

def standard_deviation():
    print("Standard Deviation: ", df['Marks'].std())

def graph():
    Mp.figure(figsize= (12, 8))
    Mp.bar(df.Student, df.Marks)
    Mp.title("Graph for Marks vs Student: ")
    Mp.xlabel("Students")
    Mp.ylabel("Marks")
    Mp.show()

print("Welcome to Student Marks Analysis!")
print("1. Mean")
print("2. Median")
print("3. Mode")
print("4. Variance")
print("5. Standard deviation")
print("6. Report")
while (True):
    Opt= int(input("Enter your choice: "))
    match Opt:
        case 1:
            mean()
        case 2:
            median()
        case 3:
            mode()
        case 4:
            variance()
        case 5:
            standard_deviation()
        case 6:
            graph()
        case 7:
            print("Exiting the loop...")
            break
        case _:
            print("Invalid option!")