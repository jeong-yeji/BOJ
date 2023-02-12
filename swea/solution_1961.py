for t in range(1, int(input()) + 1):
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    # 90
    list90 = []
    for j in range(n):
        s = ''
        for i in range(n - 1, -1, -1):
            s += str(matrix[i][j])
        list90.append(s)

    # 180
    list180 = []
    for i in range(n - 1, -1, -1):
        s = ''
        for j in range(n - 1, -1, -1):
            s += str(matrix[i][j])
        list180.append(s)

    # 270
    list270 = []
    for j in range(n - 1, -1, -1):
        s = ''
        for i in range(n):
            s += str(matrix[i][j])
        list270.append(s)

    # print
    print(f'#{t}')
    for i in range(n):
        print(f'{list90[i]} {list180[i]} {list270[i]}')
