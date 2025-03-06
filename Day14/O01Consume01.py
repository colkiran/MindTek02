
import mymodule as md
from mymodule import greet, Employee, funLogger
from abc import ABC, abstractmethod

print(f"Guest Name :{md.gname}")

print("-" * 60)

print(f"Sports :{md.sports}")

print("-" * 60)

print(f"Runs :{md.runs}")

print("-" * 60)

greet("Kholi")

print("-" * 60)

emp1 = Employee("JACK", 185000)
print(emp1)

print("-" * 60)

@funLogger
def mul(x, y):
    print(f"Product of {x} and {y}")
    return x * y

mul(10, 50)