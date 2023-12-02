# exist(sum(a, b) == 100) ? 1 : 0

arr = [False] * 101
result = 0

len = int(input())  # len <= 1000
for _ in range(len):
    i = int(input())  # 0 <= number <= 100
    if arr[100 - i]:
        result = 1
    arr[i] = True

print(result)
