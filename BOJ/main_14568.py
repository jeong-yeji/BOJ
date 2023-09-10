n = int(input())

answer = 0

for a in range(1, n):
    for b in range(1, n):
        for c in range(2, n, 2):
            if a + b + c == n and a >= b + 2:
                answer += 1
print(answer)