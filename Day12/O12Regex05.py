import re

st = "baaaat"

res = re.search(r'ba{5}t', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found....")
