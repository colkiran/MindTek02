
gname = "Sachin Tendulkar"

# list
sports = ['cricket', 'tennis', 'hockey', 'boxing', 'badmiton', 'volley ball', 'swimming']

# dictionary
runs = {'odi': 18700, 'test': 14350, 't20': 1400}

# function
def greet(gst):
    print(f"Greetings Mr.{gst}, Welcome to the event.....")


# class
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

def funLogger(fnc):

    def innerFun(*args):
        print("logging into the service.....")
        print(fnc(*args))
        print("Logging out of the service....")
        print("-" * 60)

    return innerFun



if __name__ == '__main__':

    print("-" * 60)

    print("Module name :", __name__)         # prints the name of the current module '__main__'

    print("-" * 60)

    greet(gname)

    print("-" * 60)

    emp1 = Employee("Kevin", 85000)
    print(emp1)     # call __str__()

    print("-" * 60)