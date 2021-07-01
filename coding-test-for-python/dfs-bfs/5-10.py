# 음료수 얼려 먹기


def solution(n, m, tray):
    ice = []
    for t in tray:
        ice.append(list(map(int, t)))

    def dfs(x, y):
        # 범위를 벗어나면 종료
        if x < 0 or x >= n or y < 0 or y >= m:
            return False

        if ice[x][y] == 0:
            ice[x][y] = 1  # 방문 처리
            # 상하좌우 방문
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True

        return False

    answer = 0
    # 모든 노드에 대해 음료수 채우기
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 dfs 수행
            if dfs(i, j) == True:
                answer += 1

    return answer


print(solution(3, 3, ["001", "010", "101"]))
print(solution(4, 5, ["00110", "00011", "11111", "00000"]))
print(
    solution(
        15,
        14,
        [
            "00000111100000",
            "11111101111110",
            "11011101101110",
            "11011101100000",
            "11011111111111",
            "11011111111100",
            "11000000011111",
            "01111111111111",
            "00000000011111",
            "01111111111000",
            "00011111111000",
            "00000001111000",
            "11111111110011",
            "11100011111111",
            "11100011111111",
        ],
    )
)
