"""
comparison operators
--------------------
1. equal to (mandatory)
2. greater than

"""
from functools import total_ordering

@total_ordering
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # it works for not equal to also
    def __eq__(self, other):
        return self.salary == other.salary

    # works for less than also
    def __gt__(self, other):
        return self.salary > other.salary


emp1 = Employee('Jones', 85000)
# emp1.get_details()
print("-" * 60)

print(emp1)             # will implicitly call __str__

print("-" * 60)
# type conversion operator - str
print(str(emp1))

print("-" * 60)
emp2 = Employee('Jack', 65000)
print(emp2)

print("-" * 60)
# print(emp1 == emp2)       # comparison is on objects address
print("-" * 60)
if emp1 != emp2:
    print("{}'s salary of {} is NOT equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is equal to {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))


print("-" * 60)
if emp1 < emp2:
    print("{}'s salary of {} is less than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{}'s salary of {} is greater than {}'s salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 60)

print(emp1 >= emp2)
