
def add(x, y):
    return x + y

a = add
res = a(100, 200)
print(f"res :{res}")

print("-" * 60)

b = lambda i, j :i + j
res = b(40, 60)
print(f"res :{res}")

print("-" * 60)
# lambdas are best used with  - a. map   b. filter   c. reduce

print("map".center(60, "-"))
# map function will take the expression from lambda adn implement on all values passed to it

lst1 = list(range(1, 11))
print(f"lst1 :{lst1}")

squares = list(map(lambda x : x ** 2, lst1))
print(f"squares :{squares}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")
words = list(map(lambda x : x.upper(), sentence.split()))
print(f"words :{words}")

print("filter".center(60, "-"))
lst1 = list(range(1, 31))
print(f"lst1 :{lst1}")

res_even = list(filter(lambda x : x % 2 == 0, lst1))
print(f"Enven Numbers :{res_even}")

res_three = list(filter(lambda x : x % 3 == 0, lst1))
print(f"Multiples of Three :{res_three}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 60)
res = list(filter(lambda x : x != 'the', sentence.split()))
print(f"res :{res}")

print("-" * 60)
res = list(filter(lambda x : len(x) == 3, sentence.split()))
print(f"res :{res}")

print("reduce".center(60, "-"))
from functools import reduce

lst1 = [8, 4, 1, 6, 3, 5, 2, 9, 7, 10]
print(f"lst1 :{lst1}")

res_lar = reduce(lambda x, y: x if x > y else y, lst1)
print(f'Largest :{res_lar}')

res_sum = reduce(lambda x, y: x + y, lst1)
print(f"sum of all numbers :{res_sum}")
