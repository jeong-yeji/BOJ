for t in range(int(input())):
    n = input()
    print(f'#{t + 1}', end=' ')
    print(int(n == n[::-1]))
