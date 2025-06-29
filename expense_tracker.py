# Expense Tracker with NumPy
import numpy as et

month = int(input("Enter the number of months: "))
salary= int(input("Enter your monthly salary: "))
print("\n")
expenses = et.zeros((month,6))

for i in range(month):
    Car_Exp= int(input(f"Enter Car Expenses for Month {i+1}: "))
    House_rent= int(input(f"Enter House Expenses for Month {i+1}: " ))
    Elec_Bill= int(input(f"Enter Electrical Expenses for Month {i+1}: "))
    Food_Bevr= int(input(f"Enter Food and Beverages Expenses for Month {i+1}: "))
    Healthcare= int(input(f"Enter the healthcare expenses for Month {i+1}: "))
    Trips= int(input(f"Enter expenses on trips for Month {i+1}: "))
    expenses[i]= [Car_Exp, House_rent, Elec_Bill, Food_Bevr, Healthcare, Trips]
    print("\n")

for i in range(month):
    Total= et.sum(expenses[i])
    print(f"The Total Expense Of Month {i+1} is : {Total}")
    Savings= salary-Total
    print(f"The money saved in Month {i+1}: {Savings}")
    Avg= et.average(expenses[i])
    print(f"The Average Expense Of Month {i+1} is : {Avg}")
    Max= et.max(expenses[i])
    print(f"The Maximum Expense Of Month {i+1} is : {Max}")
    Min= et.min(expenses[i])
    print(f"The Minimum Expense Of Month {i+1} is : {Min}")
    print("\n")

print("\n")
print("\t\t\tREPORT :\n", expenses)
print("\n")
print(f"Total expense in {month} months: ",expenses.sum())
print(f"The average expense in {month} months: ", expenses.mean())
print(f"The maximum expense in {month} months is: ", expenses.max())