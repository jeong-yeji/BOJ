n = int(input())
arr = list(map(int, input().split()))
x = int(input())

setarr = set(arr)

result = 0
for i in arr:
    if x - i in setarr:
        result += 1

print(result // 2)
