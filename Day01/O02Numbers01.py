
a = 10
b = -10

print(f"a :{a}")        # f string or format string - interpolation
print(type(a))          # RTTI - Run Time Type Indentification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.3
d = -10.3

print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = 2e3
f = -2e3

print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 10 + 3j
h = 10 - 3j

print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 60)
print(max(34, 56, 23, 63))
print(min(34, 56, 23, 63))

print("-" * 60)
x = 2 + 3.5
print(f"x :{x}")

print("-" * 60)
x = 2
y = 3.5
z = x + y

print(f"x = {type(x)}")
print(f"y = {type(y)}")
print(f"z = {type(z)}")

print("conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(f"11 :{11}")          # Decimal
print(f"0b11 :{0b11}")      # Binary
print(f"0b101 :{0b101}")    # Binary
print(f"0o11  :{0o11}")     # octal
print(f"0o101 :{0o101}")    # octal
print(f"0xe   :{0xe}")      # hexa
print(F"0xa   :{0xa}")      # hexa

print("Number System Coversion".center(60, '-'))
a = 100
print(f"a :{a}")
print(f"bin(a) :{bin(a)}")
print(f"oct(a) :{oct(a)}")
print(f"hex(a) :{hex(a)}")
