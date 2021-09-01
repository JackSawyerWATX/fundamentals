class User:
    def __init__(self,first_name,last_name,email,account_balance=0):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = f"{first_name} {last_name}"
        self.email = email
        self.account_balance = account_balance
    
    def display_user_balance(self):
        print(f"{self.full_name}: {self.account_balance}")
        print(f"email: {self.email}")

Jack = User("Jack","Sawyer","jack.sawyer@peanut.com")
Bobby = User("Bobby","Kennedy","robert.kennedy@senate.gov",account_balance=100)
Lyndon = User("Lyndon","Johnson","lyndon.johnson@whitehouse.gov",500)

Jack.display_user_balance()
Bobby.display_user_balance()
Lyndon.display_user_balance()