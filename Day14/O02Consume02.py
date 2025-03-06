
from mypackage.mymodule import Employee, funLogger

emp1 = Employee("Grace", 120000)
print(emp1)

print("-" * 60)

@funLogger
def diff(x, y):
    print(f'Difference of {x} and {y}')
    return x - y

diff(20, 8)