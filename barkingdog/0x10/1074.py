def recur(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    if r < half and c < half:
        return recur(n - 1, r, c)
    elif r < half and c >= half:
        return half * half + recur(n - 1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + recur(n - 1, r - half, c)
    elif r >= half and c >= half:
        return 3 * half * half + recur(n - 1, r - half, c - half)


print(recur(*map(int, input().split())))
