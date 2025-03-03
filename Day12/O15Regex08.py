import re

st = "boat"

res = re.search(r'b(oa|es|ea)t', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found....")
