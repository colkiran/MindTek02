
# strings can be enclosed in ''  or ""

print("hello world")
print('hello world')

print("-" * 60)
print("hello world \n" * 3)

print("-" * 60)
print('hello world \n' * 3)

print("-" * 60)
st1 = """
the quick brown fox jumps over the lazy dog.the quick brown fox jumps over the lazy dog. the quick brown fox jumps over the lazy dog
"""
print(f"st1 :{st1}")

print("-" * 60)
st2 = '''
the quick brown fox jumps over the lazy dog.the quick brown fox jumps over the lazy dog. the quick brown fox jumps over the lazy dog
'''
print(f"st2 :{st2}")

print("-" * 60)

st = "hello world"
print(f"st :{st}")

print(f"st[0] :{st[0]}")        # strings are stored like arrays that can be indexed
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing
print(f"st[0:5]  :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:11:2] :{st[0:11:2]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

print("-" * 60)
# reverse indexing
print(f"st[-1]  :{st[-1]}")
print(f"st[-5]  :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 60)
# slicing
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

print("-" * 60)
# check if the given string is a palindrome
st = "malayalam"

print("Palindrome" if st[:] == st[::-1] else "Not a Palindrome")

print("-" * 60)
st = "hello world"
print(f"st :{st}")
print(type(st))

# res = st.upper()
# print(res)


# st[0] = "H"
# print(st[0])
#
print("-" * 60)
print(dir(st))