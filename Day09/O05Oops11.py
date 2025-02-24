
class Employee:

    def __init__(self, name):
        self.name = name
        self.tech = ['C++', 'Java', 'J2ee', 'Spring', 'Hibernate', 'Angular JS', 'React JS']

    def __iter__(self):
        return iter(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, val):
        self.tech[index] = val

emp1 = Employee("Richard")
print("-" * 60)

print([e1 for e1 in emp1])
print("-" * 60)

emp1.append('Python')
print([e1 for e1 in emp1])

print("-" * 60)
res = emp1[2]
print(f"res :{res}")

print("-" * 60)
emp1[2] = 'JSP'
print([e1 for e1 in emp1])
