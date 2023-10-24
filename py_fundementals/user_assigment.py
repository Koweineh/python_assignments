class Account:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance
        print("Account of " + self.username)

    def make_deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def make_withdraw(self, amount):
        if amount > 0 and self.balance > amount:
            self.balance -= amount

        else:
            print("your account balance is not sufficient")

    def statement(self):
        print("hello {} your current balance is {}".format(self.name, self.balance))

    def make_display(self, amount):
        self.balance = amount

    def make_transfer(self, amount, username):
        self.balance = self.balance - amount
        username.balance = username.balance + amount
        return username.balance()


user_1 = Account("karam", 10000)
user_2 = Account("xxx", 2000)
user_3 = Account("yyy", 3000)

user_1.make_deposit(100)
user_1.make_deposit(100)
user_1.make_deposit(100)
user_1.make_withdraw(100)

user_2.make_deposit(1000)
user_2.make_deposit(1000)
user_2.make_withdraw(100)
user_2.make_withdraw(100)

user_3.make_deposit(10000)
user_3.make_withdraw(100)
user_3.make_withdraw(100)
user_3.make_transfer(1000, user_1.balance)

print(user_1.balance)
print(user_2.balance)
print(user_3.balance)
