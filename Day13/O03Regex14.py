
# \A and \Z
import re

st = "this is a sample string"

# \A string starting word
# res = re.search(r'\Athis', st)

# \Z string ending word
res = re.search(r'string\Z', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found....")


