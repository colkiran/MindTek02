
import re

st = 'good blood bad blood'

# \2 - recall the second grouping - datatype and data should be the same
res = re.search(r'(\w+)\s(\w+)\s(\w+)\s(\2)', st)

if res:
    print("Match found.....")
    print(res.group(0))
    print(res.group(1))     # first grouping
    print(res.group(2))     # second grouping
    print(res.group(3))     # third grouping
    print(res.group(4))     # fourth grouping

else:
    print("Match not found....")


