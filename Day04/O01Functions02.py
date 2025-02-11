
def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithCalc(20, 8)
print(f"res :{res}")

print("-" * 60)
# doc string

def fun():
    # this is a comment
    "This is a doc string"
    print("hello world")

fun()

print("-" * 60)
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    function fun1
    -------------
    Takes two arguments x and y,
    1. if x and y are integers then we get the sum of x and y
    2. if x and y are strings then gets concatenated string as result
    3. if x and y are two different data types then throws an error
    """
    return x + y

print(fun1(10, 20))
print(fun1("hello ", "world"))
# print(fun1(10, "abc"))

print("-" * 60)
help(fun1)
