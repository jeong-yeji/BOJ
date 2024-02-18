import sys

input = sys.stdin.readline


def sol1(n, c, houses):
    s, e = 1, (houses[-1] - houses[0]) // (c - 1) + 1
    while s < e:
        mid = (s + e + 1) // 2
        cur, cnt = houses[0], 1

        for i in range(1, n):
            if houses[i] >= cur + mid:
                cur, cnt = houses[i], cnt + 1

        if cnt >= c:
            s = mid
        else:
            e = mid - 1
    return s


if __name__ == "__main__":
    n, c = map(int, input().split())
    houses = sorted(int(input()) for _ in range(n))
    print(sol1(n, c, houses))
