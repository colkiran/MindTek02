
def fun():
    x = 1
    print("Apples from ooty....")
    yield x
    x += 9
    print("Oranges from Kanpur....")
    yield x
    x += 10
    print("grapes from hubli.....")
    yield x

# print(fun())
y = fun()
print(type(y))

print("-" * 60)
print(y.__next__())

print("-" * 60)
print(y.__next__())

print("-" * 60)
print(next(y))      # same as y.__next__()

# print(next(y))
