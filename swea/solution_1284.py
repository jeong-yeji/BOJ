for t in range(int(input())):
    p, q, r, s, w = map(int, input().split())
    a = p * w
    b = q
    if r < w:
        b += s * (w - r)
    print(f'#{t + 1} {min(a, b)}')
