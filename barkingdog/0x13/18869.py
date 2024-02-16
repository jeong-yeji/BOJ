import collections

m, n, = map(int, input().split())
origin_space = [list(map(int, input().split())) for _ in range(m)]
compress_space = collections.defaultdict(int)
for space in origin_space:
    zipped_space = {v: str(i) for i, v in enumerate(sorted(set(space)))}
    compress_space[''.join(zipped_space[planet] for planet in space)] += 1
ans = sum(c * (c - 1) // 2 for o, c in compress_space.items())
print(ans)
