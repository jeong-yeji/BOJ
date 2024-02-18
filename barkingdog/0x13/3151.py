import bisect
import sys
from collections import defaultdict

input = sys.stdin.readline


def sol1(n, scores):
    cnt = 0
    for i in range(n - 2):
        s, e = i + 1, n - 1
        while s < e:
            if scores[s] + scores[e] + scores[i] > 0:
                e -= 1
            else:
                if scores[s] + scores[e] + scores[i] == 0:
                    if scores[s] == scores[e]:
                        cnt += e - s
                    else:
                        cnt += e - bisect.bisect_left(scores, scores[e]) + 1
                s += 1
    return cnt


def sol2(scores):
    counter = defaultdict(int)
    for score in scores:
        counter[score] += 1

    keys = sorted(counter.keys())

    cnt = 0
    for i in range(len(keys)):
        x = keys[i]
        for j in range(i, len(keys)):
            y = keys[j]
            z = -(x + y)

            a, b, c = counter[x], counter[y], counter[z]

            if z < y or c == 0:
                continue

            if x == y == z and a >= 3:
                cnt += a * (a - 1) * (a - 2) // 6
            elif x == y and a >= 2:
                cnt += (a * (a - 1) // 2) * c
            elif y == z and b >= 2:
                cnt += a * (b * (b - 1) // 2)
            elif x != y and y != z:
                cnt += a * b * c
    return cnt


if __name__ == "__main__":
    n = int(input())
    scores = sorted(map(int, input().split()))
    print(sol1(n, scores))
    print(sol2(scores))
