
print("keys".center(60, "-"))
player = {'name': 'Sachin', 'age': 34, 'runs': 125, 'oppnt': 'Aus', 'venue': 'gabaa'}
print(f"player :{player}")

ky = player.keys()
print(f"keys :{ky}")

print("-" * 60)
for k in player.keys():
    print(k, "=>", player[k])

print("values".center(60, "-"))
player = {'name': 'Sachin', 'age': 34, 'runs': 125, 'oppnt': 'Aus', 'venue': 'gabaa'}
print(f"player :{player}")

vl = player.values()
print(f"values :{vl}")

print('items'.center(60, "-"))
# items is a combination of keys and values

emp = {
    'emp1': {'name': 'Mike', 'age': 35, 'desig': 'BDM', 'dept': 'MKT', 'salary': 85000},
    'emp2': {'name': 'Alen', 'age': 32, 'desig': 'TL', 'dept': 'finance', 'salary': 120000},
    'emp3': {'name': 'Tina', 'age': 28, 'desig': 'SE', 'dept': 'IT', 'salary': 145000}
}

print(f"emp :{emp}")

print("-" * 60)
print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 60)
for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("get".center(60, "-"))
emp1 = {'name': 'Mike', 'age': 35, 'desig': 'BDM', 'dept': 'MKT', 'salary': 85000}

print(f"emp1 :{emp1}")

print("-" * 60)
print(f"Department :{emp1.get('dept', 'Invalid key, Please enter  a valid key')}")
print(f"Salary     :{emp1.get('salry', 'Invalid key, Please enter  a valid key')}")

print("fromkeys".center(60, '-'))
cities = ['blr', 'che', 'mum', 'del', 'hyd', 'mum', 'kol']
print(f'Cities :{cities}')

# convert the list cities into a dictionary
res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 24)
print(f"res2 :{res2}")

print("setdefault".center(60, "-"))
# will only add new key value to the dictionary
emp1 = {'name': 'Mike', 'age': 35, 'desig': 'BDM', 'dept': 'MKT'}
print(f"emp1 :{emp1}")

emp1.setdefault('name', 'Micheal')
emp1.setdefault('age', 40)

emp1.setdefault('salary',110000)
emp1.setdefault('gender', 'Male')


print(f"emp1 :{emp1}")

