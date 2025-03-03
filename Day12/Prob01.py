import re

lno = "LCNO-KAR-72-2021-0000"

res = re.search(r'LCNO-(KAR|KER|APN|TND|MAH|TLN)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})-(?!0000)([0-9]{4})$', lno)

if res:
    print("Match found....")
    print(res.group(0))
else:
    print("Match not found....")
