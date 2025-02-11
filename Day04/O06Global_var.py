
glbX = 100

def fun(x):             # x is a local variable
    global glbX
    print(f"x :{x}")
    glbX = 500
    print(f"glbX inside :{glbX}")


print(f"glbX before the function call :{glbX}")
fun(10)
print(f"glbX after the function call  :{glbX}")
