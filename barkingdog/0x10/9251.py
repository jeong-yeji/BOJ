import sys

input = lambda: sys.stdin.readline().strip()


def sol1(A, B):
    dp = [[0] * 1001 for _ in range(1001)]
    for i, a in enumerate(A, start=1):
        for j, b in enumerate(B, start=1):
            if a == b:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(A)][len(B)]


def sol2(A, B):
    dp = [0] * len(B)
    for i, a in enumerate(A):
        cnt = 0
        for j, b in enumerate(B):
            if cnt < dp[j]:
                cnt = dp[j]
            elif a == b:
                dp[j] = cnt + 1
    return max(dp)


if __name__ == "__main__":
    A, B = input(), input()
    print(sol1(A, B))
    print(sol2(A, B))
