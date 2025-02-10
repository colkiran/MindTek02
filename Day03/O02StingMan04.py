
# Conversions
print("{val} {val} {val}".format(val='A'))
print("{val!s} {val!r} {val!a}".format(val='A'))

print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36343242342))
print("The number {num:10} {num:f} {num:b}".format(num=36))

print("Alignment".center(60, "-"))
print("{num:15}Tendulkar".format(num=36))
print("{num:15}Tendulkar".format(num="Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))
from math import pi, e
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("-" * 60)
print("{num:>15} Tendulkar".format(num="Sachin"))       # right
print("{num:^15} Tendulkar".format(num="Sachin"))       # center
print("{num:<15} Tendulkar".format(num="Sachin"))       # left

print("{num:-^60}".format(num="Python Training"))       # left
print("Python Training".center(60, "-"))

print("{pi:010.3}".format(pi=pi))
print("{pi:010.4}".format(pi=pi))
print("{pi:010.5}".format(pi=pi))

print("-" * 60)
print("{0:10.2f}\t{1:10.2f}".format(pi, -pi))
print("{0:=10.2f}\t{1:=10.2f}".format(-pi, -pi))
print("{0:=010.2f}\t{1:=010.2f}".format(-pi, -pi))

width = 50
price_width = 10
item_width = width - price_width


