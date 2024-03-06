import sys
from collections import deque

input = sys.stdin.readline


def bfs(n, graph):
    dist = [-1] * (n + 1)
    dist[1] = 0
    queue = deque([1])
    while queue:
        i = queue.popleft()
        for j in graph[i]:
            if dist[j] == -1 or dist[j] > dist[i] + 1:
                queue.append(j)
                dist[j] = dist[i] + 1
    return sum(1 for i in range(2, n + 1) if 0 < dist[i] <= 2)


def find(graph):
    friends = set(graph[1])
    if not friends:
        return 0

    for friend in list(friends):
        for f in graph[friend]:
            friends.add(f)
    return len(friends) - 1


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
print(bfs(n, graph))
print(find(graph))
