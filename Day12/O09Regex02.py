
import re

st = "hello world"

# check if the string st starts with hello
# res = re.match(r'^hello', st)

# check if the string ends with world
res = re.search(r'world$', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found....")
