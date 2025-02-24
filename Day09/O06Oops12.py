
class Employee:

    def __init__(self, name):
        self.__name = name
        self.tech = ['C++', 'Java', 'J2ee', 'Spring', 'Hibernate', 'Angular JS', 'React JS']

    def __str__(self):
        return self.__name + " - " + ", ".join([str(tech) for tech in self.tech])


emp1 = Employee("steeve")
print(emp1)

print("-" * 60)
# access the private variable outside the class
# we have to know how is it getting stored in __dict__
print(emp1.__dict__)   # _Employee__name

emp1._Employee__name = "Samuel"
print(f"emp1 :{emp1}")
print("-" * 60)

print(emp1.__dict__)
