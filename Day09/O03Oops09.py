
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return (f"Name is {self.name}\nSalary is {self.salary}")

    def __add__(self, other):
        return Employee("Noname", self.salary + other.salary)

    def __sub__(self, other):
        return Employee("Noname", self.salary - other.salary)

    def __mul__(self, other):
        return Employee("Noname", self.salary * other.salary)

    def __truediv__(self, other):
        return Employee("Noname", self.salary / other.salary)

    def __floordiv__(self, other):
        return Employee("Noname", self.salary // other.salary)


emp1 = Employee("Mark", 150)
emp2 = Employee('John', 250)
emp3 = Employee("Joe", 100)
print(emp1)
print("-" * 60)

print(emp2)
print("-" * 60)

print(emp3)


print("-" * 60)
# add
print(emp1 + emp2 + emp3)

print("-" * 60)
print(emp2 - emp1)

print("-" * 60)
print(emp1 * emp2)

print("-" * 60)
print(emp1 / emp3)

print("-" * 60)
print(emp1 // emp3)