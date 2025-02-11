def outerFun():
    gname = "Sachin"            # local var
    def innerFun():

        nonlocal gname          # only local variable can be converted to non_local variables
        print("Hello World")
        gname += " Tendulkar"
        print(f"Greetings Mr.{gname}")

    innerFun()
    print(f"After the call to innerFun from outerFun :{gname}")

outerFun()

