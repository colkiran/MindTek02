import re

st = "baaat"

res = re.search(r'ba{3,5}t', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found....")
