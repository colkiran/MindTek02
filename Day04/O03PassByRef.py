
stud = ['Daniel', 'Mike', 'John', 'Peter', 'Slater', 'Kevin']

def attendance(lst):
    print(f"lst before :{lst}")
    # absent
    lst.pop(3)
    lst.pop(-1)
    print(f"lst after :{lst}")


print(f"stud before :{stud}")
attendance(stud)
print(f"stud after  :{stud}")