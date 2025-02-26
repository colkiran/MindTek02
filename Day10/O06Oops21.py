
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's job.....")

class Developer(Employee):

    def doJob(self):
        print("Coding job......")


def BankJob(emp):
    print("Bank Job Started........")
    emp.doJob()
    print("Bank Job Ended.........")
    print("-" * 60)


mike = Manager()
david = Developer()

BankJob(mike)
BankJob(david)
