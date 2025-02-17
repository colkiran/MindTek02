"""
sort    - sort will sort the original list
sorted  - sorted will take a copy of the list sorts it and returns it
"""
print(f"sort".center(60, '-'))
l1 = [8, 5, 9, 6, 1 , 4, 10, 3, 7, 2]
print(f"l1 :{l1}")

res_asc = sorted(l1)
res_desc = sorted(l1, reverse = True)

print(f"Ascending order  :{res_asc}")
print(f"Descending order :{res_desc}")

print("-" * 60)
l1 = [8, 'zebra', 'apple', 5, 'white', 'blue', 9, 'yellow', 6, 'green', 1, 'violet', 4, 'pink',  10,  'maroon', 3, 'red', 7, 'bat', 2, 'cat', 'umbrella', 'dog', 187, 1234, 27, 215, 2301]

print(f"l1 :{l1}")

print("-" * 60)
res_asc = sorted(l1, key = ascii)
print(f"Ascending order :{res_asc}")

for i in range(0, len(res_asc)):
    if type(res_asc[i]) == int:
        print(i)
        break

print("-" * 60)
print(res_asc[:14] + sorted(res_asc[14:]))

print("-" * 60)
cities = ['thiruvananthapuram', 'pune', 'bangalore', 'mysore', 'vishakapatnam', 'chennai', 'mumbai', 'delhi', 'ooty', 'hyderabad']
print(f"cities :{cities}")

print("-" * 60)
# sort the cities based on the length
res_asc = sorted(cities, key=len)
print(f"Ascending order :{res_asc}")

print("reverse".center(60, "-"))
l1 = [8, 5, 9, 6, 1 , 4, 10, 3, 7, 2]
print(f"l1 :{l1}")

print("-" * 60)
res = list(reversed(l1))
print(f"res :{res}")

