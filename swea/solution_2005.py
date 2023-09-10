for t in range(int(input())):
    n = int(input())
    triangle = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            triangle[i][j] = 1

    for i in range(1, n):
        for j in range(1, n):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

    print(f'#{t + 1}')
    for i in range(n):
        print(' '.join(map(str, triangle[i][:i + 1])))
