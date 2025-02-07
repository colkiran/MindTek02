
st = "hello world"
print(f"st :{st}")

print("-" * 60)
# capitalize
res = st.capitalize()
print(res)

print("-" * 60)
# title
res = st.title()
print(res)

print("-" * 60)
# upper
res = st.upper()
print(res)

print("-" * 60)
st = "*****hello******"
print(f"st :{st}")

print("-" * 60)
# lstrip
res = st.lstrip("*")
print(f"res :{res}")

print("-" * 60)
# rstrip
res = st.rstrip("*")
print(f"res :{res}")

print("-" * 60)
# strip
res = st.strip("*")
print(f"res :{res}")

print("-" * 60)
# replace
st = "hello world"
print(f"st :{st}")

res = st.replace("h", "H")
print(f"res: {res}")

res = st.replace("l", "L")
print(f"res :{res}")

res = st.replace("l", "L", 1)
print(f"res :{res}")

res = st.replace("l", "L", 2)
print(f"res :{res}")

print("-" * 60)
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

res = st.replace("fox", "tiger")
print(f"res :{res}")

res = st.replace("t", "T", 1)
print(f"res :{res}")
