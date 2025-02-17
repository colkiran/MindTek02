
print("append".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")

print("extend".center(60, "-"))
l2 = list(range(6, 11))
print(f"l2 :{l2}")

l2.extend([11, 12, 13, 14])
print(f"l2 :{l2}")

l2.extend([15])
print(F"l2 :{l2}")

print("insert".center(60, "-"))
l2.insert(1, 6.5)
l2.insert(2, 7.5)
l2.insert(3, 8.5)

print(f"l2 :{l2}")

print("pop".center(60, "-"))
# pop function returns the value that was discarded from the list

l1 = list(['blr', 'che', 'mum', 'del', 'kol', 'hyd'])
print(f"l1 :{l1}")

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop(-1)
print(f"res :{res}")

# pop's the last element from the list
res = l1.pop()
print(f"res :{res}")


print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = [1, 2, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 2, 3, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1]
print(f"l1 :{l1}")

print("-" * 60)
l1.remove(3)
print(f"l1 :{l1}")

# l1.remove(5)
print("-" * 60)
while 1 in l1:
    l1.remove(1)

print(f"l1 :{l1}")

print("clear".center(60, "-"))
l1 = list(range(1, 16))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")




