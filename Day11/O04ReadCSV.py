
import csv
from prettytable import PrettyTable


with open("Employee.csv", "r") as CSVR:
    emp_details = csv.reader(CSVR)
    prtyTbl = PrettyTable(next(emp_details))

    for row in emp_details:
        prtyTbl.add_row(row)


print(prtyTbl)


    # print(emp_details)
    # colnames = next(emp_details)            # read the first line
    # print(*colnames)
    #
    # for line in emp_details:
    #     print(*line)
