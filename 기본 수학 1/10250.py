# ACM 호텔
for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n % h == 0:
        print("{}{:02d}".format(h, n // h))
    else:
        print("{}{:02d}".format(n % h, n // h + 1))
