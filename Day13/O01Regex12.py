
# \d and \D

import re

st = "The mobile !@#$%  ^&*()+ number is 902323348 which is not reachable"

# extracts all numeric data
# res = re.search(r'\d+', st)

# matches all non numeric data
res = re.search(r'\D+', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")
