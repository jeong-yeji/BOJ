for i in range(int(input())):
    numbers = list(map(int, input().split()))
    res = sum(numbers) / 10
    print(f'#{i + 1} {round(res)}')
