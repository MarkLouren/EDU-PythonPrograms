class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance=min_balance

    def deposit(self, amount):
        self.balance += amount
    def withdraw (self, amount):
        if self.balance-amount>=self.min_balance:
            self.balance-=amount
        else:
            print("Sorry, no Funds!")
    def statement(self):
        print ("Account Balance: ${}".format(self.balance))

class Current (Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    # change displaying class in print
    def __str__(self):
        return "{}'s Current Account: Balance ${}".format(self.name, self.balance)

class Savings (Account):
    def __init__(self, name, balance):
        super().__init__(name,balance,min_balance=0)

    # change displaying class in print
    def __str__(self):
         return "{}'s Saving Account: Balance ${}".format(self.name, self.balance)


x=Current("Vova", 5000)
x.deposit(3100)
y=Savings ("Me", 300)
print (y)
