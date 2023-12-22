from itertools import combinations

while True:
    numbers = list(map(int, input().split()))
    if numbers[0] == 0:
        break

    for combination in combinations(numbers[1:], 6):
        print(*combination)
    print()
