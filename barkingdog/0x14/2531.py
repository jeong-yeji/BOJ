import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().strip()


def sol1(n, d, k, c, sushi):
    cnt = defaultdict(int)
    cnt[c] = 1
    for i in range(k):
        cnt[sushi[i]] += 1

    ans = len(cnt)
    for i in range(n):
        if cnt[sushi[i]] == 1:
            del cnt[sushi[i]]
        else:
            cnt[sushi[i]] -= 1
        cnt[sushi[i + k]] += 1

        ans = max(ans, len(cnt))
        if ans == d or ans == k + 1:
            break

    return ans


def sol2(n, d, k, c, sushi):
    check = [0] * (d + 1)

    check[c] += 1
    cnt = ans = 1
    for i in range(k):
        check[sushi[i]] += 1
        cnt += check[sushi[i]] == 1

    for i in range(0, n):
        check[sushi[i]] -= 1
        cnt -= check[sushi[i]] == 0
        check[sushi[i + k]] += 1
        cnt += check[sushi[i + k]] == 1
        ans = max(ans, cnt)

    return ans


if __name__ == "__main__":
    n, d, k, c = map(int, input().split())
    sushi = [int(input()) for _ in range(n)] * 2
    print(sol1(n, d, k, c, sushi))
    print(sol2(n, d, k, c, sushi))
