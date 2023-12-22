n = int(input())
cnt = 0
is_used = [[False] * 30 for _ in range(3)]


def recur(k):
    global n, cnt
    if k == n:
        cnt += 1
        return

    for i in range(n):
        if is_used[0][i] or is_used[1][i + k] or is_used[2][k - i + n - 1]:
            continue

        is_used[0][i] = True
        is_used[1][i + k] = True
        is_used[2][k - i + n - 1] = True
        recur(k + 1)
        is_used[0][i] = False
        is_used[1][i + k] = False
        is_used[2][k - i + n - 1] = False


recur(0)
print(cnt)
