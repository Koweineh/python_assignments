# has function to show user details
# child class : Bank
# Stores details about the account balance
# Stores details about the amount
# Allows for deposits,withdraw,view_balance


# Parent class
class User:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def show_details(self):
        print("Personal Details")
        print(" ")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# Child class
class Bank(User):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
        self.balance = 0

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("You have Deposited : " ,self.balance)
        
        
    def withdraw(self,amount):
        self.amount = amount 
        if self.amount > self.balance:
            print("Insufficient funds : Balance available : " ,self.balance)
        else:
            self.balance = self.balance - self.amount
            print("You have Withdrawn : " ,self.withdraw)       
        
    def view_balance(self):
        self.show_details()   
        print("Your current account balance is  : " ,self.balance)    \
            
            
            


karam = Bank("Karam", "Male", "37")
karam.deposit(1000)
karam.deposit(1000)
karam.withdraw(500)
karam.view_balance()

