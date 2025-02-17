
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)

l2 = [1, 2, 3, 4.2, 5.0, 6.9, 'seven', 'eight', 'nine', 10+3j, 11-2j, True, False]
print(f"l2 :{l2}")
print(type(l2))
print("-" * 60)

l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD

# create
l1 = list(range(1, 16))
print(f"l1 :{l1}")

# read
print(f"l1[2] :{l1[2]}")
print(f"l1[-1] :{l1[-1]}")

for i in range(1, len(l1), 1):
    print(i, end=" ")

# update = update the list l1 - add new values, modify the existing values

print(f"l1 :{l1}")
print(f"l1[2] :{l1[2]}")
l1[2] = 300
print(f"l1 :{l1}")
l1[10] = 9
print(f"l1 :{l1}")

print("-" * 60)
# delete
print(f"l1 :{l1}")
del l1[2]
del l1[-1]

print(f"l1 :{l1}")

print("-" * 60)
# print(dir(l1))


