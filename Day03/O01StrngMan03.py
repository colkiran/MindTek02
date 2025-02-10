"""
1. index
2. count
3. maketrans and translate
"""

print("index".center(60, "-"))
st = "hello world"
print(f"st :{st}")
print(f"st.index('h') :{st.index('h')}")

print(f"st.index('w') :{st.index('w')}")
print(f"st.index('l') :{st.index('l')}")
print(f"st.index('l') :{st.index('l', st.index('l') + 1)}")
print(f"st.index('l') :{st.index('l', st.index('l', st.index('l') + 1) + 1)}")

print("count".center(60, "-"))
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")

print(f"e :{st.count('e')}")
print(f"o :{st.count('o')}")

print("maketrans".center(60, "-"))
st = "hello world"
print(f"st :{st}")
# length of a and b should be the same
a = 'helowrd'
b = 'HELOWRD'

resTbl = st.maketrans(a, b)
print(resTbl)

print("translate".center(60, "-"))
res = st.translate(resTbl)
print(f"res :{res}")

print("formatting".center(60, "-"))
# c style formatting
format = "Welcome %s, what a %s player"
print(format)
values = ("Sachin", "superb")
print(values)

print("-" * 60)
print(format, values)

print("-" * 60)
print(format % values)

print("-" * 60)
format = "Welcome %s, your rating of %.3f, what a %s player...."
print(format % ("Sachin", 4, "class"))
print(format % ("Sachin", 4.7888999, "class"))
print(format % ("Sachin", 4.8, "class"))
print(format % ("Sachin", 4.899342346, "class"))

print("-" * 60)
print("Welcome %s, your rating of %.3F, What a %s player" % ("Sachin", 4.82383, "class"))

# unix Style
from string import Template
tmpl = Template("Welcome $name, What a $adj player")
print(tmpl)
print(tmpl.substitute(name="Sachin", adj="class"))
print("-" * 60)

# format of python string
print("Welcome {}, what a {} player for {}".format("Sachin", "superb", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "superb", "India"))
print("Welcome {2}, what a {0} player for {1}".format("Sachin", "superb", "India"))
print("Welcome {pname}, with a rating of {rating} what a {adj} player for {ctry}".format(pname = "Sachin", rating=4, adj="superb", ctry="India"))
print("Welcome {pname}, with a rating of {rating:.3f} what a {adj} player for {ctry}".format(pname = "Sachin", rating=4.7999392, adj="superb", ctry="India"))

# interpolation
from math import pi, e
print(f"PI= {pi} and Eulers constant = {e}")

print("-" * 60)
print("PI = {}  and Euler constant = {}".format(pi, e))

print("-" * 60)
full_name = ['Sachin', 'Tendulkar']
print(f"name :{full_name}")

print("Mr.{name}".format(name=full_name))
print("Mr.{name[0]} {name[1]}".format(name = full_name))

print("-" * 60)
import math
# dunder name
print(__name__)     # prints the name of the current module - __main__
print(math.__name__)

print("The {mod.__name__} module gives the value of pi = {mod.pi} and eulers constant = {mod.e}".format(mod=math))
