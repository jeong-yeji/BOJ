import sys


def check():
    global N, H
    line = list(range(N + 1))
    for i in range(1, H + 1):
        for j in horizontal[i]:
            line[j], line[j + 1] = line[j + 1], line[j]
    return all(line[i] == i for i in range(1, N + 1))


def put(max_depth, cur_depth, x, y):
    global N, M, H
    if max_depth == cur_depth:
        return cur_depth if check() else -1

    if sum(i % 2 for i in installed) <= 3 - cur_depth:
        for i in range(x, H + 1):
            for j in range(y if i == x else 1, N):
                if all(j + offset not in horizontal[i] for offset in [-1, 0, 1]):
                    horizontal[i].add(j)
                    installed[j] += 1
                    ret = put(max_depth, cur_depth + 1, i, j)
                    if ret != -1:
                        return ret
                    horizontal[i].remove(j)
                    installed[j] -= 1

    return -1


input = lambda: sys.stdin.readline().strip()

N, M, H = map(int, input().split())

installed = [0] * (N + 1)  # 각 세로선에 설치된 사다리의 개수
horizontal = [set() for _ in range(H + 1)]  # 각 높이에 설치된 사다리가 접하는 세로줄
for _ in range(M):
    a, b = map(int, input().split())
    horizontal[a].add(b)
    installed[b] += 1

for depth in range(4):
    answer = put(depth, 0, 1, 1)
    if answer != -1:
        print(answer)
        break
else:
    print(-1)
