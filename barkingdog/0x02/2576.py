sum = 0
min = 100

for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        sum += n
        if n < min:
            min = n


if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
