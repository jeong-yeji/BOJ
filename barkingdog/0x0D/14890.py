import sys


def is_available(line):
    global n, l
    bridge = [False] * n
    for i in range(1, n):
        if abs(line[i - 1] - line[i]) > 1:
            return False

        if line[i - 1] == line[i]:
            continue

        if line[i - 1] - line[i] > 0:
            if i + l > n:
                return False
            for j in range(l):
                if line[i] != line[i + j] or bridge[i + j]:
                    return False
                bridge[i + j] = True
        else:
            if i - l < 0:
                return False
            for j in range(l):
                if line[i - 1] != line[i - 1 - j] or bridge[i - 1 - j]:
                    return False
                bridge[i - 1 - j] = True
    return True


input = lambda: sys.stdin.readline().strip()
n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for row in board:
    answer += is_available(row)
for col in list(zip(*board[::-1])):
    answer += is_available(col)
print(answer)
