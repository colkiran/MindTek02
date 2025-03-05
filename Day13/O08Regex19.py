

import re
st = 'the quick brown fox jumps over the lazy dog.'

print(f"st :{st}")

res = re.sub('the', 'The', st, count= 1)

print(f'res :{res}')

print("-" * 60)

st = """
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
the quick brown fox jumps over the lazy dog.
"""

for line in st.splitlines():
    res = re.sub(r'the', 'The', line, count=1 )
    print(res)


