for t in range(int(input())):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))

    flag = True

    for line in sudoku:
        if sum(line) != 45:
            flag = False
            break

    if flag:
        for j in range(9):
            s = 0
            for i in range(9):
                s += sudoku[i][j]
            if s != 45:
                flag = False
                break

    if flag:
        dr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
        dc = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = 0
                for k in range(9):
                    s += sudoku[i + dr[k]][j + dc[k]]
                if s != 45:
                    flag = False
                    break

    print(f'#{t + 1} {int(flag)}')
