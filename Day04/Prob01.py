"""
1. st = "the quick brown fox jumps over the lazy dog"

write a code to check how many times each letter in the string is repeated

"""
from collections import Counter

st = "the quick brown fox jumps over theeeee lazy dog that"
print(f"st :{st}")
print(type(st))
print(len(st))

print("-" * 60)
s1 = set(st)
print(s1)
print(len(s1))

chr_count = {}
for i in s1:
    if i != " ":
        chr_count[i] = st.count(i)

print(chr_count)

print("-" * 60)
res = Counter(st)
print(res)
