
age = int(input("Enter the age :"))

try:
    if age < 18:
        raise ValueError("Age should be greater than 18 to cast the vote....")

    print("you can cast your vote......")

except ValueError as v:
    print(v)
    print(v.__class__)

finally:
    print("Completed the task of voting.....")