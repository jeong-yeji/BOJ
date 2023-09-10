# 최댓값
list = []
for _ in range(9):
    list.append(int(input()))
# list = [int(input()) for i in range(9)]

print(max(list))
print(list.index(max(list)) + 1)
