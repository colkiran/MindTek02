
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))
print("-" * 60)

d2 = {'name': 'sachin', 'runs': 120, 'oppnt': 'WI', 'venue': 'Sabina Park'}
print(f"d2 :{d2}")
print(type(d2))
print("-" * 60)

d3 = dict([('name', 'rahul'), ('age', 32), ('runs', 89), ('oppn', 'eng')])
print(f"d3: {d3}")
print(type(d3))
print("-" * 60)

d4 = dict(name='sourav', age=34, runs=92, oppnt='Nzl')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 60)
# CRUD

# create
player = {'name': 'Sachin', 'age': 34, 'runs': 56, 'oppnt': 'Aus'}
print(f"player :{player}")

print("-" * 60)
# read
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 60)
# iterate
for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# update - modify, add a element
# modify
player['name'] = "Tendulkar"
player['runs'] = 135
# add new elements
player['venue'] = 'perth'
player['year'] = 2003

print(f"player :{player}")

print("-" * 60)
# delete
del player['age']
del player['oppnt']

print(f"player :{player}")

print("-" * 60)
print(dir(player))
