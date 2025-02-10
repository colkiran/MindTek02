
"""
6. write a code to generate
1
23
456
78910

"""
x = 1
for i in range(1, 5):
    for j in range(i):
        print(x, end="")
        x += 1
    print()
