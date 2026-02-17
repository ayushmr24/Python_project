from datetime import datetime
 
class BankAccount:
 
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.history = []   # transaction history list
 
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.history.append(("Deposit", amount, datetime.now()))
        else:
            print("Invalid amount")
 
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.history.append(("Withdraw", amount, datetime.now()))
        else:
            print("Insufficient balance or invalid amount")
 
    def get_balance(self):
        return self.balance
 
    def transfer(self, amount, target_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
 
            self.history.append(("Transfer Out", amount, datetime.now()))
            target_account.history.append(("Transfer In", amount, datetime.now()))
        else:
            print("Transfer failed")
 
    def __str__(self):
        return f"Account {self.acc_no} | Name: {self.name} | Balance: {self.balance}"
a1 = BankAccount(101, "Shashank", 1000)
a2 = BankAccount(102, "Rahul", 500)
 
a1.deposit(200)
a1.withdraw(150)
a1.transfer(300, a2)
 
print(a1)
print(a2)
 
print("\nTransaction History of a1:")
for t in a1.history:
    print(t)
