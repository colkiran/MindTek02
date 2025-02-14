
def outerFun():

    print("outer function code.....01")
    def innerFun():

        print("inner function code.....")
        print("Hello World")

    print("outer function code.....02")

    innerFun()

    print("outer function code.....03")

outerFun()

