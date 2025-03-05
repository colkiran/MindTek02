
# \b and \B

import re

st = "this is an  SAMPLE exsample text"

# re.I ignore the case
# this will search 'sample' as a seperate word
# res = re.search(r'\bsample', st, re.I)

# sample as substring - non word boundary
res = re.search(r'\Bsample', st, re.I)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")
