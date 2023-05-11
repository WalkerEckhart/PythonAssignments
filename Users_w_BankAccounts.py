class BankAccount:
    def __init__(self,int_rate=1.02, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance}")
        return self
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance <= 0:
            self.balance += amount
            print("Insufficient funds ({self.balance}). $5 share fee incurring...")
            self.balance -= 5
        print(f"Balance: ${self.balance}")
        return self
    
    def display_account_info(self):
        print(f"User: {self.first_name} {self.last_name} /// Total Balance: ${self.balance} /// AIA (Annual Interest Accrual): {self.int_rate}%")
        
        return self
    def yield_interest(self):
        self.balance *= self.int_rate
        return self
    
class User():
    def __init__(self, first_name, last_name, dob="2020202020", email="@@@@@@"):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.account = BankAccount(int_rate=1.02, balance=0)
        self.savings = BankAccount()
        self.checking = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"Balance: ${self.account.balance}")
        return self

    
user_walker = User("walker", "e", "December 26, 2001", "yabbadabbado@rockyroad.rock")
user_walker.make_deposit(3).make_withdraw(6).display_user_balance()