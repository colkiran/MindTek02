
try:

    n = int(input("Enter the number :"))
    d = int(input("Enter the divisor :"))

    res = n / d

except TypeError as t:
    print(t)            # message
    print(t.__class__)
except ZeroDivisionError as z:
    print(z)
    print(z.__class__)
except Exception as e:
    print("Exception caught....")
    print(e)
    print(e.__class__)
else:
    print(f"res :{res}")

finally:
    print("Division of numbers completed.....")

print("-" * 60)
print("hello world \n" * 10)
