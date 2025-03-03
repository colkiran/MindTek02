# . (dot) can represent only one character - alpha_numeric and special characters

import re

st  = "b*t"

# r'' = raw string
res = re.match(r'b.t', st)

# if it matches res will have some data else res is null
if res:
    print("Match found....")
    # prints the string that matched our regex
    print(res.group(0))
else:
    print("Match not found....")
