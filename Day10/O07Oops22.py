# duck types

class Manager:
    def doJob(self):
        print("Manager's Job.......")


class Developer:

    def doJob(self):
        print("Coding job......")

mike = Manager()
david = Developer()

def BankFunJobs(emps):      # polymorphism
    print("Bank job strarted.......")
    for emp in emps:
        emp.doJob()
    print("Completed".center(60, "-"))
    print("-" * 60)

BankFunJobs([mike, david])
