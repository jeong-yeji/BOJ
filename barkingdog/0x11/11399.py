from itertools import accumulate


def sol1():
    n = int(input())
    p = sorted(map(int, input().split()))
    print(sum(accumulate(p)))


def sol2():
    n = int(input())
    P = sorted(map(int, input().split()))
    res, ans = 0, 0
    for p in P:
        ans += res + p
        res = res + p
    print(ans)


if __name__ == "__main__":
    sol1()
    sol2()
