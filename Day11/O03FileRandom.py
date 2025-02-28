
FL = open("data.txt", "rb")

# returns the position of the file handle
print(FL.tell())

pos = FL.seek(75, 0)
print(f"Position :{pos}")

pos = FL.seek(45, 1)
print(f"Position :{pos}")

st = FL.read(30)
print(FL.tell())

pos = FL.seek(85, 0)
print(f"Position :{pos}")

pos = FL.seek(75, 1)
print(f"Position :{pos}")

pos = FL.seek(-50, 1)
print(f"Position :{pos}")

pos = FL.seek(200, 2)
print(f"Position :{pos}")

pos = FL.seek(-300, 2)
print(f"Position :{pos}")


# Throws an error
# pos = FL.seek(-50, 0)
# print(f"Position :{pos}")



FL.close()