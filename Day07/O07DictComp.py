
lst = [1, 2, 3, 4, 5]
print(f"lst :{lst}")

res = [x ** 2 for x in lst]
print(f"res :{res}")
print("-" * 60)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(f"dict1 :{dict1}")
print("-" * 60)

dict2 = {item for item in dict1}
print(f"dict2 :{dict2}")
print("-" * 60)

dict3 = {item for item in dict1.keys()}
print(f"dict3 :{dict3}")
print("-" * 60)

dict4 = {item for item in dict1.values()}
print(f"dict4 :{dict4}")
print("-" * 60)

dict5 = {item for item in dict1.items()}
print(f"dict5 :{dict5}")
print("-" * 60)

dict6 = {k: v for (k, v) in dict1.items()}
print(f"dict6 :{dict6}")
print("-" * 60)

dict7 = {k: v * 2 for (k, v) in dict1.items()}
print(f"dict7 :{dict7}")
print("-" * 60)

dict8 = {v * 2: k for (k, v) in dict1.items()}
print(f"dict8 :{dict8}")
print("-" * 60)

girls = ['tina', 'mary', 'lisa', 'margret']
boys = ['mike', 'slater', 'steve', 'kevin']
print(f"girls :{girls}")
print(f"boys :{boys}")

dict9 = dict(zip(boys, girls))
print(f"dict9 :{dict9}")
print("-" * 60)

dict10 = {k: v for k, v in zip(boys, girls)}
print(f"dict10 :{dict10}")
print("-" * 60)

squares = {x : x ** 2 for x in range(1, 11)}
print(f"squares :{squares}")
