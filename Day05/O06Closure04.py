
def fun(*args):
    print(args)
    print(*args)
    print("-" * 60)

fun()
fun(10)
fun(10, 20)
fun(10, 20, 30)
fun(10, 20, 30, 40)

print("-" * 60)

def sum(x, y):
    print(f"adding {x} and {y}")
    return x + y

def diff(x, y):
    print(f"subtracting {y} form {x}")
    return x - y


def log_details(fnc):
    loginfo = "Logging into the service....."

    def innerFun(*args):
        print(loginfo)
        print(fnc(*args))
        print("-" * 60)

    return innerFun

sumLogger = log_details(sum)
sumLogger(37, 82)

diffLogger = log_details(diff)
diffLogger(88, 31)

