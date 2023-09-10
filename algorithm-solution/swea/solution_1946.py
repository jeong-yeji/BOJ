for t in range(1, int(input()) + 1):
    zipped = ''
    for _ in range(int(input())):
        c, k = input().split()
        zipped += c * int(k)

    print(f'#{t}')
    for i in range(0, len(zipped), 10):
        print(zipped[i:i + 10])
