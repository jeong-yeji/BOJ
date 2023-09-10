for t in range(1, int(input()) + 1):
    numbers = list(map(int, input().split()))
    res = (sum(numbers) - max(numbers) - min(numbers)) / 8
    print(f'#{t} {round(res)}')
