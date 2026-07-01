#ABANDONED got too lazy 2 fix it


class Account:
    def __init__(self, name, ID, balance):
        self.name = name
        self.ID = ID
        self.balance = balance
        self.frozen = False
        self.history = []

    def validate_amount(self, amount):
        if not isinstance(amount, int):
            return 'Amount must be an integer'
        
    def save_transaction(self, amount):
        return f'{amount}'
    
    def deposit(self, amount, description=None):
        if self.frozen is True:
            return False
        self.balance += amount
        if description:
            self.history.append(f'{description}: +${amount}')
            return True
        else:
            self.history.append(f'Deposit: +${amount}')
            return True
        
    def withdraw(self, amount, description=None):
        if self.frozen is True:
            return False
        if amount > self.balance:
            return False
        self.balance -= amount
        if description:
            self.history.append(f'{description}: +-{amount}')
            return True
        else:
            self.history.append(f'Withdrawal: -${amount}')
            return True

    def toggle_freeze(self):
        if self.frozen:
            self.frozen = False
        else:
            self.frozen = True
    
    @property
    def account_status(self):
        if self.frozen:
            return 'Frozen'
        else:
            return 'Not Frozen'

    def __str__(self):
        return f'Name: {self.name} | ID: {self.ID} | Balance: {self.balance} | Status: {self.account_status}'

class Vault:
    def __init__(self):
        self.accounts = []
    
    def validate_ID(self, text=None):
        try:
            if text:
                ID= int(input(text+'\n'))
            else:
                ID = int(input('Enter ID:\n'))
        except ValueError:
            return False
        if ID < 0:
            return False
        return ID
    
    def create_ID(self):
        ID = self.validate_ID()
        print(ID, type(ID))
        for account in self.accounts:
            if account.ID == ID:
                return False
        return ID
    
    def validate_balance(self):
        try:
            balance = int(input('Enter Balance:\n'))
        except ValueError:
            return False
        if balance < 0:
            return False
        return balance
    
    def create_account(self):
        name = input('Enter Name:\n').lower()
        ID = self.create_ID()
        if ID is False:
            return 'ID must be a positive integer'
        balance = self.validate_balance()
        if balance is False:
            return 'Balance must be a positive integer'
        account = Account(name, ID, balance)
        self.accounts.append(account)
        return 'Account created successfully!'

    def find_account(self, ID):
        for account in self.accounts:
            if account.ID == ID:
                return account
        return False

    def view_accounts(self):
        final = ''
        for account in self.accounts:
            final += str(account) +'\n'
        return final
    
    def validate_amount(self, text=None):
        try:
            if text:
                amount = int(input(text+'\n'))
            else:
                amount = int(input('Enter Amount:\n'))
        except ValueError:
            return False
        if amount < 0:
            return False
        return amount

    def deposit(self):
        amount = self.validate_amount()
        if amount is False:
            return 'Amount must be a positive integer'
        account_id = self.create_ID()
        account = self.find_account(account_id)
        if account is False:
            return 'Unable to find account'
        print(type(account))
        account.deposit(amount)
        return
        if success is False:
            return 'Unable to Complete Deposit'
        else:
            return 'Depost Successful!'

    def withdraw(self):
        amount = self.validate_amount
        ID = self.create_ID()
        account = self.find_account(ID)
        success = account.withdraw(amount)
        if success is False:
            return 'Unable to complete withdraw'
        else:
            return 'Withdrawal Successful!' 

    def transfer(self):
        amount = self.validate_amount('Enter amount you wish to transfer')
        # Transfer Amount ^^^
        from_id = self.create_ID('Enter withdrawal account ID:')
        from_account = self.find_account(from_id)
        from_account.withdraw(amount)
        #  Finding and withdrawing from the "from_id" account ^^^
        to_id = self.create_ID('Enter deposit account ID')
        to_account = self.find_account(to_id)
        to_account.deposit(amount)
        # Finding and Depositing money into the "to_id" account ^^^
        return 'Transfer Complete!'


def run():
    Bank = Vault()
    is_running = True
    print('====================\nVault\n====================')
    while is_running:
        print('-----\n1. Create Account\n2. View Accounts\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Freeze Account\n7. View Transaction History\n8. Quit')
        choice = input()
        if choice =='1':
            execute = Bank.create_account()
            print(execute)
        elif choice =='2':
            print(Bank.view_accounts())
        elif choice =='3':
            print(Bank.deposit())
        elif choice =='4':
            print(Bank.withdraw())
        elif choice == '5':
            print(Bank.transfer())
        elif choice =='8':
            is_running = False
            print('Session Terminated')
        else:
            pass
run()
        
            