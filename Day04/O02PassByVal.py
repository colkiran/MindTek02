
def fun(x):
    print(f"x inside before :{x}")
    x += 150
    print(f"x inside after :{x}")

y = 100
print(f"y before :{y}")
fun(y)
print(f"y after  :{y}")
