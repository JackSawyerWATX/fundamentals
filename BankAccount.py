class BankAccount:
    bank_name = "Fifty-Third National"
    all_accounts = []
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
            #self.balance = self.balance - amount
            return self
    
    def display_account_info(self):
        print (f"balance {self.balance}")
        print (f"intrest rate {self.int_rate}")
        return self
    
    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest
        return self
    
    def display_all_users(cls):
        for i in cls.all_accounts:
            i.display_account_info("balance")

Jack = BankAccount (.03, 500)
Jack.deposit(50).withdraw(100).display_account_info().yield_interest()
print (Jack.balance)

#deposit(self, amount) - increases the account balance by the given amount
#withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
#display_account_info(self) - print to the console: eg. "Balance: $100"
#yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)