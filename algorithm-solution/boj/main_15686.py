from itertools import combinations
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
city = []
houses = []
chickens = []
for i in range(n):
    city.append(list(map(int, input().split())))
    for j in range(n):
        if city[i][j] == 1:
            houses.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

combi = combinations(list(range(len(chickens))), m)
res = sys.maxsize
for c in combi:
    chicken_distance = 0
    for house in houses:
        distance = sys.maxsize
        for idx in list(c):
            d = abs(house[0] - chickens[idx][0]) + abs(house[1] - chickens[idx][1])
            distance = min(distance, d)
        chicken_distance += distance
    res = min(res, chicken_distance)

print(res)
