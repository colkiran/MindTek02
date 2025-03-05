
"""
Requirement

with money from the account:
    a. balance in the account should not be less than 1000
    b. user account will be blocked for 24 hours if the user enter a wrong pin three times

"""

import time

class BalanceExceptionError(Exception):

    def __init__(self):
        print("Insufficient Balance.......")

class AttemptExceptionError(Exception):

    def __init__(self):
        print("Too many attempts, your account is blocked for 24 hours......")


attempts = 1
def withdraw():
    global attempts
    balance = 10000
    saved_pin = 4321
    pin = int(input("Enter the PIN :"))
    if pin == saved_pin:
        try:
            amt = float(input("Enter the amount to be withdrawn :"))
            temp_bal = balance - amt
            if temp_bal < 1000:
                raise BalanceExceptionError
            balance = balance - amt
            print(f"Amount {amt} debited from the account successfully...")
            print(f"Balance in the account is :{balance}")
        except Exception as var:
            print(var)
            print(var.__class__)
    else:
        ans = input("Do you want to re-enter the PIN (y/n) :")
        if ans.lower() == 'y':
            attempts += 1
            # print(f"hello.....{attempts}")
            try:
                if attempts == 4:
                    raise AttemptExceptionError
            except Exception as var:
                print(var)
                print(var.__class__)
                time.sleep(86400)
            else:
                withdraw()
        else:
            print("Thank you....")
            return

withdraw()

