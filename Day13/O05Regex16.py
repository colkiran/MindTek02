
import re

st = "the quick brown fox jumps over the lazy dog."

res = re.search(r'fox', st)

if res:
    print("Match found.....")
     # res.start() - index where the regex matched
    print("String that got rejected by regex -", st[:res.start()])
    print("String that matched our regex     -", res.group(0))
    # res.end() - gives the last index that matched the regex
    print("String not checked by regex       -", st[res.end():])
else:
    print("Match not found....")


