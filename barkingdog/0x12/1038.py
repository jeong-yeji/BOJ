from itertools import combinations

result = []
for i in range(1, 11):
    for j in combinations(range(10), i):
        result.append(int(''.join(map(str, reversed(list(j))))))
result.sort()

n = int(input())
print(result[n] if n < len(result) else -1)
