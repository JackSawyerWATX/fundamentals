class BankAccount:
    bank_name = "Thirty-Sixth National"
    all_accounts = []
    def __init__(self,first_name,last_name,email,int_rate,balance):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.email = email
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def display_user_balance(self):
        print(f"{self.full_name}: {self.account_balance}")
        print(f"email: {self.email}")

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
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

Robert = BankAccount("Robert","McNamara","robert.mcnamara@wardepartment.gov",250000)
Dean = BankAccount("Dean","Rusk","dean.rusk@statedepartment.gov",200000)
Bobby = BankAccount("Bobby","Kennedy","robert.kennedy@attorneygeneral.gov",100000)
Lyndon = BankAccount("Lyndon","Johnson","lyndon.johnson@whitehouse.gov",500000)
John = BankAccount("John","Kennedy","john.kennedy@whitehouse.gov",750000)
User = BankAccount (.03, 500)
User.deposit(50).withdraw(100).display_account_info().yield_interest()
print (User.balance)