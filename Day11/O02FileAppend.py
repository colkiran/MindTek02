
# opening the file in append mode
FA = open("myfile.txt", "a")

st = input("Enter the contents for the file :")
FA.write(st + "\n")

FA.close()