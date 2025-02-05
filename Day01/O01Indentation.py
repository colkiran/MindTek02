
"""
indentations are used
1. for loop
2. if condition
3. function
4. class

"""

print("This is main function code...")

def fun():
    print("Function code......")

fun()

for i in range(1, 11):
    print(i, end=" ")

print()

x = 10
if x < 10:
    print("sigle digit number....")
    if x > 5:
        print("x is more than half of 10")
else:
    print("not a single digit number")
