import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (n + 1)
queue = deque([1])
visited[1] = 1
while queue:
    i = queue.popleft()
    for j in graph[i]:
        if not visited[j]:
            queue.append(j)
            visited[j] = 1
print(sum(visited) - 1)
