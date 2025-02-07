
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 60)

for j in range(i, 0, -1):
    print(j, end=" ")
print()

print("-" * 60)

for i in range(1, 31):
    # if i > 25:
    #     break
    if i % 2 == 1:
        continue
    print(i, end=" ")
else:
    print("\nCompleted generating numbers....")

print("-" * 60)

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


print("-" * 60)
for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")
    print()





