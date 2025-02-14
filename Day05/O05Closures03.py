
def outerFun(greet):

    def innerFun(sep):

        def innerMostFun(gname):
            from emojis import emojis

            emojized = emojis.encode(greet + " :"  + sep + ": " + gname)

            print(emojized)

        return innerMostFun

    return innerFun

kanGrt = outerFun("Namaskara")

kanGrtTgr = kanGrt("tiger")

kanGrtTgr("Prabhakar")


"""
engGrt = outerFun("Hello")
kanGrt = outerFun("Namaskara")

engGrtSngArw = engGrt("------->")
engGrtDblArw = engGrt("======>>")
kanGrtSngArw = kanGrt('------->')

engGrtSngArw("Sachin")
engGrtDblArw("Rahul")
kanGrtSngArw("Anil")
"""