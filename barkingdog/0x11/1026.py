n = int(input())
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()))
print(sum(a * b for a, b in zip(A, B)))
