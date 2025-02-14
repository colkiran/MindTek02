
def outerFun():
    gname = "Sachin Tendulkar"
    def innerFun():
        print(f"Greetings Mr.{gname}")

    return innerFun

outerFun()()

print("-" * 60)

inref = outerFun()
inref()

