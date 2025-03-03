import re

st = "bat"

# works with any alpha_numeric character
# res = re.search(r'b[a-zA-Z0-9]t', st)

# any vowel
# res = re.search(r'b[aeiou]t', st)

# should not be a vowel
res = re.search(r'b[^aeiou]t', st)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found....")
