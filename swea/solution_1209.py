for _ in range(10):
    t = int(input())
    sums = []
    columns = [0] * 100
    numbers = []

    for _ in range(100):
        line = list(map(int, input().split()))
        numbers.append(line)

        # row
        sums.append(sum(line))

        # column
        for i in range(100):
            columns[i] += line[i]

    # cross
    cross = 0
    for i in range(100):
        cross += numbers[i][i]
    sums.append(cross)

    sums += columns

    print(f'#{t} {max(sums)}')
