import collections
import sys

d = collections.defaultdict(int)
for i in sys.stdin.readlines()[1:]:
    d[int(i.strip())] += 1
print(sorted(d.items(), key=lambda x: (-x[1], x[0]))[0][0])
