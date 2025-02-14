
def outerFun(fnc):

    def helper(amt):
        print("Logging into the DB....")
        fnc(amt)
        print("Logging out of the DB....")
        print('-' * 60)

    return helper

def deposit(x):
    print(f"Amount {x} deposited successfully into the account.....")

helperRef = outerFun(deposit)
helperRef(5000)

print('-' * 60)

# deposit is a variable name
deposit = outerFun(deposit)
deposit(10000)          # calls the innerFun

print('-' * 60)

@outerFun           # withdraw = outerFun(withdraw)
def withdraw(y):
    print(f"Amount {y} successfully debited from the account....")

withdraw(4500)          # calls the innerFun
