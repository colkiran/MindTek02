
def outerFun(greet):

    # simple curry
    def innerFun(gname):

        print(greet, gname)

    return innerFun

outerFun("Hello")("Sachin")

print("-" * 60)

engGrt = outerFun("Hello")
kanGrt = outerFun("Namaskara")

engGrt("Sachin")
kanGrt("Rahul")

