class Bank:
    def __init__(self,interest_rate =0.1,balance=0):
    
        self.interest_rate = interest_rate 
        self.balance = balance

    def deposit(self,amount):
         if amount > 0:
            self.balance += amount
            
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            self.balance -=5
            print("your account balance is not sufficient",self.balance)
            return False
        
    def statement(self,name):
        print("hello {} your current balance is {}".format(name, self.balance))


    def transfer(self, amount, username):
       if self.withdraw(amount):
        username.deposit(amount)
    



class User:
    def __init__(self, username ):
        self.username = username
        self.account =Bank(1000)
      
        print("Account of " + self.username)

    def make_deposit(self, amount):
        self.account.deposit(amount)

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
    

    def statement(self):
        self.account.statement(self.name)


    def make_transfer(self, amount, username):
        self.account.transfer(amount, username)


user_1 = User("karam")
user_2 = User("xxx")
user_3 =User("yyy")

user_1.make_deposit(1000)
user_1.make_transfer(100,user_2.account)

print(user_1.account.balance)
print(user_2.account.balance)
print(user_3.account.balance)
