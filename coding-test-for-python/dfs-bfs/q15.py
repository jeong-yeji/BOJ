# 특정 거리의 도시 찾기

from collections import deque


def solution(n, m, k, x, way):
    answer = []
    visited = [False] * (n + 1)
    path = [[] for _ in range(n + 1)]
    for a, b in way:
        path[a].append(b)

    queue = deque()
    queue.append((x, 0))
    while queue:
        num, cnt = queue.popleft()

        if cnt == k:
            answer.append(num)
        elif cnt < k:
            for i in path[num]:
                if not visited[i]:
                    visited[i] = True
                    queue.append((i, cnt + 1))

    return -1 if len(answer) == 0 else sorted(answer)


way = [[1, 2], [1, 3], [2, 3], [2, 4]]
print(solution(4, 4, 2, 1, way))

way = [[1, 2], [1, 3], [1, 4]]
print(solution(4, 3, 2, 1, way))

way = [[1, 2], [1, 3], [2, 3], [2, 4]]
print(solution(4, 4, 1, 1, way))
