import bisect


def dp(n, arr):
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def bs(n, arr):
    dp = [arr[0]]
    for i in range(n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            idx = bisect.bisect_left(dp, arr[i])
            dp[idx] = arr[i]
    return len(dp)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    # print(dp(n, arr))
    print(bs(n, arr))
