
sqaures = [x ** 2 for x in range(1, 11)]
print(f"squares :{sqaures}")

fruits = [
    ('apple', 285),
    ('orange', 85),
    ('pineapple', 60),
    ('grapes', 135),
    ('banana', 70),
    ('gauva', 110),
    ('pears', 210),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")
print("-" * 60)

price = ["fruit" for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit[0] for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit[1] for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit[1] * 0.9 for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

pirce = [fruit[1] * 0.75 for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

expnsv_frt = [fruit for fruit in fruits if fruit[1] > 100]
print(f"Expensive fruits :{expnsv_frt}")
print("-" * 60)

expnsv_frt = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75] for fruit in fruits if fruit[1] > 100]
print(f"Expensive Fruits :{expnsv_frt}")
print("-" * 60)

sentence=  "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 60)
words = [word for word in sentence.split()]
print(f"words :{words}")

print("-" * 60)
words = [word for word in sentence.split() if word != 'the']
print(f"words :{words}")

print("-" * 60)
words = [word for word in sentence.split() if len(word) == 3]
print(f"words :{words}")

print("-" * 60)
girls = ['tina', 'mary', 'lisa', 'margret']
boys = ['mike', 'slater', 'steve', 'kevin']
print(f"girls :{girls}")
print(f"boys :{boys}")

print("-" * 60)
combine = [(boy, girl) for boy in boys for girl in girls]
print(combine)
