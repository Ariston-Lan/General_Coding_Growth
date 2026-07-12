#Vault Project V2. Day 42. Making this on 0 hours of sleep. 
import json
from pathlib import Path
class BankAccount:
    def __init__(self, name, id, balance):
        self._name = name
        self._id = id
        if not isinstance(balance, (float)) or balance<0:
            raise ValueError('"Balance" must be a postive number')
        else:
            self._balance = balance
    
    @property
    def name(self):
        return self._name
    
    @property
    def id(self):
        return self._id
    
    @property
    def balance(self):
        return self._balance
    
    def __str__(self):
        return f'{self.name} | {self.id} | ${self.balance}'
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError('"Name" value must be a string')
        if self.name == new_name:
            raise ValueError(f'Account already named "{new_name}"')
        self._name = new_name

    @balance.setter
    def balance(self, new_balance):
        if not isinstance(new_balance, (float)):
            raise ValueError('"Balance" must be a number')
        if new_balance<0:
            raise ValueError('"Balance" must be positive')
        self._balance = new_balance
    
    def deposit(self, amount):
        if amount<0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
    
    def withdraw(self, amount):
        if amount<0:
            raise ValueError('Withdrawal amount must be postive')
        if amount > self.balance:
            raise ValueError('Insufficient Funds')
        self.balance -= amount

class Bank:
    def __init__(self):
        self._accounts = []

    @property
    def accounts(self):
        return self._accounts
    
    def validate_id(self, id):
        for account in self.accounts:
            if account.id == id:
                raise ValueError("Account ID already taken.")
        return id
    
    def create_account(self):
        name = input("Enter Name:\n")
        id = input("Enter ID:\n")
        id = self.validate_id(id)
        balance = float(input("Enter Balance:\n"))
        account = BankAccount(name, id, balance)
        self.accounts.append(account)
        print(account)
    
    def find_account(self, id):
        for account in self.accounts:
            if account.id == id:
                return account
        raise ValueError('ID does not match any given account in database')
    
    def deposit(self):
        id = input("Enter account ID:\n")
        amount = float(input("Enter deposit amount:\n"))
        self.find_account(id).deposit(amount)
    
    def withdraw(self):
        id = input("Enter account ID:\n")
        amount = float(input("Enter withdraw amount:\n"))
        self.find_account(id).withdraw(amount)
    
    def view_account(self):
        id = input("Enter account ID:\n")
        print(self.find_account(id))
    
    def transfer(self):
        amount = float(input("Enter transfer amount:\n"))
        id_1 = input("Enter account ID transferring the money:\n")
        id_2 = input("Enter account ID receiving the money:\n")
        if id_1 == id_2:
            raise ValueError('Cannot transfer to self')
        self.find_account(id_2).deposit(amount)
        self.find_account(id_1).withdraw(amount)
        print(self.find_account(id_1))
        print(self.find_account(id_2))

def run():
    bank = Bank()
    running = True
    while running:
        print('====\n1.Create\n2.Deposit\n3.Withdraw\n4.View\n5.Transfer\n6.Quit')
        choice = input()
        try:
            if choice == '1':
                bank.create_account()
            elif choice == '2':
                bank.deposit()
            elif choice =='3':
                bank.withdraw()
            elif choice == '4':
                bank.view_account()
            elif choice =='5':
                bank.transfer()
            elif choice =='6':
                running = False
                print('Session Terminated')
        except ValueError as e:
            print(e)
run()