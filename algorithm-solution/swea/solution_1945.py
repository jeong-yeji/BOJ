divider = [2, 3, 5, 7, 11]
for t in range(int(input())):
    n = int(input())

    res = [0, 0, 0, 0, 0]
    for i in range(5):
        while n % divider[i] == 0:
            res[i] += 1
            n //= divider[i]

    print(f'#{t + 1} {res[0]} {res[1]} {res[2]} {res[3]} {res[4]}')
