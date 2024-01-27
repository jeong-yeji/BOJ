import sys

numbers = sorted(int(sys.stdin.readline().strip()) for _ in range(int(input())))
cnt, val, max_cnt, max_val = 0, numbers[0], 0, 0
for number in numbers:
    if val == number:
        cnt += 1
    else:
        cnt, val = 1, number
    if cnt > max_cnt:
        max_cnt, max_val = cnt, val
print(max_val)
