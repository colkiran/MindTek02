
l1 = [1, 1, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1 , 1, 1]
print(f"l1 :{l1}")

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"5 :{l1.count(5)}")

print("index".center(60, "-"))
l1 = [1, 1, 2, 1, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 3, 2, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1 , 1, 1]
print(f"l1 :{l1}")

print("-" * 60)
print(l1.index(3))
print(l1.index(3, l1.index(3) + 1))
print(l1.index(3, l1.index(3, l1.index(3) + 1) + 1))

print("copy".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 before :{l1}")

# we have to copy l1 to l2
l2 = l1             # shallow copy - copies the address with data

print(f"l2 before :{l2}")

l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
# copy function

l3 = list(range(10, 60, 10))
print(f"l3 before :{l3}")

# copy l3 to l4
l4 = l3.copy()              # deep copy  - copies only the values
print(f"l4 before :{l4}")

l4.extend(list(range(70, 101, 10)))
print(f"l4 after :{l4}")

print(f"l3 after :{l3}")

print("=" * 60)
l5 = [1, 2, 3, [2, 4, 6, 8, 10], 4, 5]
print(f"l5 before :{l5}")

# copy l5 to l6
l6 = l5.copy()              # deep copy
print(f"l6 before :{l6}")

l6[3].append(12)
l6[3].append(14)
l6[3].append(16)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
l7 = [1, 3, 5, 7, [10, 20, 30, 40, 50], 9]
print(f"l7 before :{l7}")

# copy l7 to l8
from copy import deepcopy           # deep copy
l8 = deepcopy(l7)

print(f"l8 before :{l8}")

l8[4].extend([60, 70, 80])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")