
print("Arithmetic Operators".center(60, "-"))
print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}")
print(f"10 % 3 = {10 % 3}")
print(f"10 ** 3 = {10 ** 3}")


print("Augmenter".center(60, "-"))

x = 10
print(f"x :{x}")

x += 5
print(f"x :{x}")

x /= 3
print(f"x :{x}")

x *= 10
print(f"x :{x}")

print("Comparison Operators".center(60, "-"))

a = 10
b = 15

print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("Logical Operators".center(60, "-"))

print(f"{1 == 1} and {2 == 2} : {1 == 1 and 2 == 2}")
print(f"{1 == 1} and {2 == 1} : {1 == 1 and 2 == 1}")

print(f"{1 == 1} or {1 == 1} : {1 == 1 or 2 == 2}")
print(f"{1 == 2} or {2 == 1} : {1 == 2 or 2 == 1}")

print(f"not({1 == 1} or {1 == 1}) : {not(1 == 1 or 2 == 2)}")
print(f"not({1 == 2} or {2 == 1}) : {not(1 == 2 or 2 == 1)}")
