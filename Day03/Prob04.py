
"""
9. generate

1 2 3 4 5
 1 2 3 4
  1 2 3
   1 2
    1
   2 1
  3 2 1
 4 3 2 1
5 4 3 2 1

"""

for i in range(5, 0, -1):
    print(" " * (5-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

for i in range(2, 6):
    print(" " * (5-i),  end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()