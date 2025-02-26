
FL = open("data.txt", "r")

# reads the entire contents of the file and returns a list of strings
# st = FL.read()
# print(st)

# reads the specified number of bytes from the file
# st = FL.read(1000)
# print(st)

# can read only one line at a time
# st = FL.readline()
# print(st)

# reads the specified number of bytes from the line (depends on the size of the line)
# st = FL.readline(852)
# print(st)

# reads all the lines from the file and returns as a string list
# st = FL.readlines()
# print(st)

# for line in FL.readlines():
#     print(line)

# reads all the lines from the beginning where the byte falls
st = FL.readlines(855)
print(st)

FL.close()