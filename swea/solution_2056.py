for i in range(int(input())):
    date = input()
    month = int(date[4:6])
    day = int(date[6:])

    flag = False
    if month == 2 and day <= 28:
        flag = True
    elif month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
        flag = True
    elif month in [4, 6, 9, 11] and day <= 30:
        flag = True

    res = f'{date[:4]}/{date[4:6]}/{date[6:]}' if flag else -1

    print(f'#{i + 1} {res}')
