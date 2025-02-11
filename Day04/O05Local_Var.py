
def fun(x):             # x is a local variable
    print(f"x inside :{x}")
    y = "hello world"   # y is also a local variable
    print(f"y inside :{y}")

fun(100)

# print(f"x outside :{x}")
print(f"y outside :{y}")