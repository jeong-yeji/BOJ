for i in range(int(input())):
    numbers = list(map(int, input().split()))
    print(f'#{i + 1} {max(numbers)}')
