from itertools import combinations

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sum_stat = [sum(i) + sum(j) for i, j in zip(arr, zip(*arr))]
all_stat = sum(sum_stat) // 2
result = 1e9
for combi in combinations(sum_stat, n // 2):
    result = min(result, abs(all_stat - sum(combi)))
print(result)
