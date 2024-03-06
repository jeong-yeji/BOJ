import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def bfs(x, dist):
    dist[x] = 0
    queue = deque([x])
    while queue:
        i = queue.popleft()
        for j in graph[i]:
            if dist[j] == -1 or dist[j] > dist[i] + 1:
                queue.append(j)
                dist[j] = dist[i] + 1


n = int(input())
graph = [[] for _ in range(n + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

candidates = defaultdict(list)
for x in range(1, n + 1):
    dist = [-1] * (n + 1)
    bfs(x, dist)
    candidates[max(dist)].append(x)

k = min(candidates.keys())
print(k, len(candidates[k]))
print(' '.join(map(str, sorted(candidates[k]))))
