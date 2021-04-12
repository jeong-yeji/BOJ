# 요세푸스 문제 0
from collections import deque

n, k = map(int, input().split())
josephus = deque([i for i in range(1, n + 1)])
res = []

while josephus:
    josephus.rotate(-(k - 1))
    res.append(josephus.popleft())

print("<", end="")
for i in range(len(res)):
    if i == len(res) - 1:
        print(res[i], end=">\n")
    else:
        print(res[i], end=", ")