a, b = input().split()
A = set(map(int, input().split()))
B = set(map(int, input().split()))
A.difference_update(B)  # new_set = A - B
print(len(A))
print(*sorted(A))
