
# single line if condition
a = int(input("Enter the value for a :"))
print(f"a :{a}")
print(type(a))      # a is an object of <int class>

if a < 10: print(f"a is a single digit number :{a}")

print("-" * 60)
b = int(input("Enter the value for b :"))
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = int(input("Enter the value for c :"))
print(f"c :{c}")
print(type(c))

print("-" * 60)

if a >= b and a >= c:
    print(f"a is the greatest :{a}")
elif b >= a and b >= c:
    print(f"b is the greatest :{b}")
else:
    print(f"c is the greatest :{c}")



