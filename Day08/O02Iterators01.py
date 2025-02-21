
l1 = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"l1 :{l1}")
print("-" * 60)
# print(dir(l1))
itrObj = l1.__iter__()
print(dir(itrObj))

print("-" * 60)
elem1 = itrObj.__next__()
print(f"elem1 :{elem1}")

elem2 = next(itrObj)
print(f"elem2 :{elem2}")
elem3 = next(itrObj)
print(f"elem3 :{elem3}")
elem4 = next(itrObj)
print(f"elem4 :{elem4}")
elem5 = next(itrObj)
print(f"elem5 :{elem5}")
elem6 = next(itrObj)
print(f"elem6 :{elem6}")

# elem7 = next(itrObj)
# print(f"elem6 :{elem6}")

print("-" * 60)
for i in l1:
    print(i, end = " ")


