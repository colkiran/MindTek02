
import time

def timeCalc(fnc):

    def innerFun(y):
        print("executing the function......")
        st = time.perf_counter()
        fnc(y)
        et = time.perf_counter()
        print("completed executing.....")
        print("-" * 60)
        print(f"The total time taken to execute the function is {round(et - st, 2)}")
        print("-" * 60)

    return innerFun


@timeCalc
def fun(x):
    lst = []
    for i in range(x):
        for j in range(i + 1):
            lst.append(j ** 3)

fun(8500)