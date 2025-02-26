# RBI has a new rule that every customer should get a facility of checking his account balance and it should be free


from abc import ABC, abstractmethod

# class given by RBI
class Account(ABC):

    def __init__(self):
        print("Account Ctor.....")

    @abstractmethod
    def get_balance(self):
        pass

    def deposit(self):
        pass

    def withdraw(self):
        pass



class Savings(Account):

    def fun(self):
        print("Hello World....")

    def get_balance(self):
        print("amount in the account ending 5453 is ######.##")

class Current(Account):

    def get_balance(self):
        pass


sav1 = Savings()
sav1.fun()
sav1.get_balance()