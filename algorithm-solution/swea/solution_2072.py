import sys

input = sys.stdin.readline

for i in range(int(input())):
    numbers = list(map(int, input().split()))
    res = sum(number for number in numbers if number % 2 == 1)
    print(f'#{i + 1} {res}')
