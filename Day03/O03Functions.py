
def greet():
    print("Greetings Mr.Sachin, Welcome to the event.....")


def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.......")


# city is called default variable and gname is called non default variable
def greetGstCty(gname, city="Mumbai", x=100):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event........")


greet()
print("-" * 60)

greetGst("Sachin")
greetGst("Rahul")

print("-" * 60)

greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 60)

def admisn(fnm, lnm, dob, gender, qlf, conno, mailid, m_status, ntnlty):
    print(f"Name           :{fnm} {lnm}")
    print(f"DOB            :{dob}")
    print(f"Gender         :{gender}")
    print(f"Qualification  :{qlf}")
    print(f"Contact No.    :{conno}")
    print(f"Email          :{mailid}")
    print(f"Marital Status :{m_status}")
    print(f"Nationality    :{ntnlty}")

# normal call - args
admisn("Rohit", "Sharma", "10/2/1989", 'Male', 'commerce graduate', '923492384', "rohit@gmail.com", "Single", "Indian")

print("-" * 60)

# keyword arguments - kwargs
admisn(dob="19/3/1990", m_status="Single", mailid='rohit@gmail.com', gender='Male', fnm="Rohit", qlf='Commerce Graduate', lnm="Sharma", conno='2394239', ntnlty='Indian')

print("-" * 60)
# variable length arguments

# *numbers can accept more than one value and stores it in numbers as a tuple ()
def productAll(*numbers):
    print(numbers)
    print(*numbers)             # unpack
    prod = 1
    for number in numbers:
        prod *= number          # prod = prod * number
    return prod

res = productAll(1, 2, 3, 4, 5)
print(res)

print("-" * 60)

# **details will store kwargs in the form of a dictionary
def extract_detail(**details):
    print(details)
    print(f"Name :{details['name']}")
    print(f"Runs :{details['runs']}")


extract_detail(name='Sachin', age=36, runs=135, opponent="Aus")     # kwargs

print("-" * 60)
# functions can return values

def multiplyMe(x, y):
    return x * y

print(f"The product of 10 and 15 is :{multiplyMe(10, 15)}")

