
def outerFun():

    def innerFun():

        print("Hello World.....")

    return innerFun

# outerFun()()            # calls the innerFun
#
# print("-" * 60)

inref = outerFun()

print("Great Day....\n" * 10)

inref()
