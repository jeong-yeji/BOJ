import itertools
import sys


def execute(directions, board):
    for direction in directions:
        for _ in range(direction):
            board = list(zip(*board[::-1]))
        merge(board)

    global answer
    answer = max(answer, max(sum(board, [])))


def merge(board):
    global n
    for idx, row in enumerate(board):
        result, merged = [], [False] * (n + 1)
        for val in row:
            if val == 0:
                continue
            if not result or merged[len(result)] or val != result[-1]:
                result.append(val)
            else:
                result[-1] *= 2
                merged[len(result)] = True
        board[idx] = result + [0] * (n - len(result))


input = lambda: sys.stdin.readline().strip()
n = int(input())
game = [list(map(int, input().split())) for _ in range(n)]
product = itertools.product([0, 1, 2, 3], repeat=5)
answer = 0
for p in product:
    execute(p, [row[:] for row in game])
print(answer)
