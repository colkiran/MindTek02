
import re

# st = "this2398#723 is a string"

st = "@#$%^ &*()!"

# word or alpha_numeric characters no special characters
# res = re.search(r'(\w+)', st)

# non word only special characters
res = re.search(r'(\W+)', st)


if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found....")
