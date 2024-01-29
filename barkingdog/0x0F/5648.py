import sys

numbers = sys.stdin.read().split()[1:]
for i in range(len(numbers)):
    numbers[i] = int(numbers[i][::-1])
numbers.sort()
print(*numbers, sep='\n')
