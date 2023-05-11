class BankAccount:
    def __init__(self, first_name, last_name, int_rate, balance): 
        self.first_name = first_name
        self.last_name = last_name
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance: ${self.balance}")
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds. $5 share fee incurring...")
            self.balance -= 5
        else:
            self.balance = self.balance - amount
        print(f"Balance: ${self.balance}")
        return self
    
    def display_account_info(self):
        print(f"User: {self.first_name} {self.last_name} /// Total Balance: ${self.balance} /// AIA (Annual Interest Accrual): {self.int_rate}%")
        
        return self
    def yield_interest(self):
        self.balance *= self.int_rate
        return self

user_walker = BankAccount("Walker", "Eckhart", 1.03, 1000)
user_link = BankAccount("Crystal", "Lenk", 1.004, 3000)

user_walker.deposit(30).deposit(30).deposit(30).withdraw(10).display_account_info()
# user_link.deposit(100).deposit(100).withdraw(20).withdraw(20).withdraw(20).withdraw(20).yield_interest().display_account_info()