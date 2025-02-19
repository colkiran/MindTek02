
print('pop'.center(60, "-"))
emp1 = {'name': 'Mike', 'age': 35, 'desig': 'BDM', 'dept': 'MKT'}
print(f"emp1 :{emp1}")

res = emp1.pop('age')
print(f"res :{res}")

res = emp1.pop('dept')
print(f"res :{res}")

# res = emp1.pop()
# print(f"res :{res}")

print(f"emp1 :{emp1}")

print("popitem".center(60, "-"))

emp1 = {'name': 'Mike', 'age': 35, 'desig': 'BDM', 'dept': 'MKT', 'salary': 120000}
print(f"emp1 :{emp1}")

res = emp1.popitem()
print(f"res :{res}")

res = emp1.popitem()
print(f"res :{res}")

print(f"emp1 :{emp1}")

print("update".center(60, "-"))

emp1 = {'name': 'Mike', 'age': 35, 'desig': 'BDM', 'dept': 'MKT'}

emp2 = {'name': 'Alen', 'age': 32, 'desig': 'TL', 'salary': 120000}

print(f'emp1 :{emp1}')
print("-" * 60)

print(f"emp2 :{emp2}")

print("-" * 60)
emp1.update(emp2)

print(f"emp1 :{emp1}")

print("copy".center(60, "-"))
d1 = {'name': 'Kenith', 'age': 30, 'loc': 'NYK'}
print(f"d1 before :{d1}")

# copy the dictionary d1 to d2
d2 = d1             # shallow copy - address is also copied
print(f"d2 before :{d2}")

d2['gender'] = 'Male'
d2['desig'] = 'TL'

print(f'd2 after :{d2}')
print(f"d1 after :{d1}")

print("=" * 60)

d3 = {'name': 'jack', 'age': 45, 'desig': 'PM'}
print(f"d3 before :{d3}")

# copy the dictionary d3 to d4
d4 = d3.copy()          # deep copy
print(f"d4 before :{d4}")

d4['salary'] = 185000
d4['dept'] = 'finance'

print(f"d4 after :{d4}")
print(f"d3 after :{d3}")

print("=" * 60)

d5 = {'name': 'jack', 'age': 45, 'desig': {'hp': 'fe', 'wipro': 'tl', 'tcs': 'fm', 'IBM': 'PM'}}

print(f"d5 before :{d5}")

# copy the dictionary d5 to d6
d6 = d5.copy()

print(f"d6 before :{d6}")

d6['desig']['microsoft'] = 'GM'
d6['desig']['dell'] = 'director'

print(f"d6 after :{d6}")
print(f"d5 after :{d5}")

print('=' * 60)
d7 = {'name': 'jack', 'age': 45, 'desig': {'hp': 'fe', 'wipro': 'tl', 'tcs': 'fm', 'IBM': 'PM'}}

print(f"d7 before :{d7}")

# copy the dictionary d7 to d8
from copy import deepcopy
d8 = deepcopy(d7)

d8['desig']['microsoft'] = 'GM'
d8['desig']['dell'] = 'director'

print(f"d8 after :{d8}")
print(f"d7 after :{d7}")