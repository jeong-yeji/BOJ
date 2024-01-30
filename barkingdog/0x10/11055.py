def sol1(n, arr):
    dp = arr[:]
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + arr[i])
    return max(dp)


def sol2(n, arr):
    dp = [0] * 1001
    for i in arr:
        dp[i] = max(dp[:i]) + i
    return max(dp)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    print(sol1(n, arr))
    print(sol2(n, arr))
