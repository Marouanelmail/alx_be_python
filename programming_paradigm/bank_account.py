#!/usr/bin/python3
class BankAccount:
    def __init__(self, account_balance) -> None:
        self.account_balance = account_balance
    
    def deposit(self, amount):
        # total_balance = self.account_balance + amount
        # return total_balance
        self.account_balance += amount
    
    def withdraw(self, amount):
        if self.account_balance < amount:
            # print ("Funds not sufficient")
            return False
        elif self.account_balance > amount:
            self.account_balance -= amount
            return True   
    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance):.2f}")
        # self.name = name
    # def printuser(self):
    #     print(f"this is {self.name} account balance : {self.account_balance}")
    # def deposit(amount):
    #     pass
# BankAccount1 = BankAccount(200, "samir")
# BankAccount1.printuser()
