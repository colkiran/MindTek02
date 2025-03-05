
class ThreeDivisionError(Exception):

    def __init__(self):
        print("ThreeDivisionError Ctor")
        print("The number cannot be divided by three(3).....")


n1 = int(input("Enter the numerator :"))
n2 = int(input("Enter the denominator :"))

try:
    if n2 == 3:
        raise ThreeDivisionError
        # raise ThreeDivisionError("Cannot divide the number by 3....")

    res = n1 / n2           # suspicious code
    print(f"res :{res}")
except ThreeDivisionError as t:
    print(t)
    print(t.__class__)
