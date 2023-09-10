for t in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(f'#{t + 1}', end=' ')
    print(' '.join(map(str, numbers)))
