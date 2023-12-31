import itertools
import sys

input = lambda: sys.stdin.readline().strip()
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

houses = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 1]
chickens = [(i, j) for i in range(n) for j in range(n) if board[i][j] == 2]

# distances = [[abs(r1 - r2) + abs(c1 - c2) for r2, c2 in chickens] for r1, c1 in houses]
distances = []
for (r1, c1) in houses:
    distance = []
    for (r2, c2) in chickens:
        distance.append(abs(r1 - r2) + abs(c1 - c2))
    distances.append(distance)

result = 100_000
for combination in itertools.combinations(range(len(chickens)), m):
    # result = min(result, sum(min([distance[i] for i in combination]) for distance in distances))
    city_distance = 0
    for distance in distances:
        city_distance += min([distance[i] for i in combination])
    result = min(result, city_distance)
print(result)
