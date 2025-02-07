
i = 1
while(i <= 10):
    print(f"hello - {i}")
    i += 1

print("-" * 60)
print(f"outside - {i}")

while(i > 0):
   print(i, end=" ")
   i -= 1
print()

print("-" * 60)
i = 1
while(True):
    print(i, end=" ")
    i += 1
    if i >= 11:
        break
