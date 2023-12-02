from math import ceil

n = list(map(int, input().replace('9', '6')))
numbers = [0] * 10
for i in n:
    numbers[i] += 1
numbers[6] = ceil(numbers[6] / 2)
print(max(numbers))
