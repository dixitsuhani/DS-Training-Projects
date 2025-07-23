# Create a class BankAccount with deposit and withdraw methods.

class BankAccount:
    def __init__(self, balance= 0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")
print("Enter To Bank !")
acc = BankAccount()
print("1 : Show Balance \n2 : Deposit Amount \n3 : Withdraw Amount \n4 : Exit the Bank ")
while (True):
    Num = int(input("Enter Your Choice : "))
    if Num == 1 :
        print("Balance:", acc.balance)
    elif Num == 2 :
        dep = int(input("Enter Amount to Deposit :"))
        acc.deposit(dep)
    elif Num == 3 :
        withd = int(input("Enter Amount to Withdraw :"))
        acc.withdraw(withd)
    elif Num == 4 :
        print("Exiting The Loop...")
        break
    else :
        print("Invalid Option !")