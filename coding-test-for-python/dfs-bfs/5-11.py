# 미로 탈출

from collections import deque


def solution(n, m, input_list):
    miro = []
    for i in input_list:
        miro.append(list(map(int, i)))

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 공간을 벗어났을 때
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                # 괴물이 있는 곳일 때
                if miro[nx][ny] == 0:
                    continue
                # 해당 노드를 처음 방문할 때 (1), 최단 거리 기록
                if miro[nx][ny] == 1:
                    miro[nx][ny] = miro[x][y] + 1
                    queue.append((nx, ny))

    bfs(0, 0)

    return miro[n - 1][m - 1]


print(solution(3, 3, ["110", "010", "011"]))
miro = ["101010", "111111", "000001", "111111", "111111"]
print(solution(5, 6, miro))