# OX 퀴즈
# 맞은 문제의 점수는 그 문제까지 연속된 O의 개수
# 방법 1
n = int(input())
list = [input() for _ in range(n)]
points = []

for l in list:
    count = 0
    point = 0

    for i in range(len(l)):
        if l[i] == "O":
            count += 1
            point += count
        else:
            count = 0

    points.append(point)

for p in points:
    print(p)

# 방법 2
n = int(input())
points = []

for _ in range(n):
    str = input()
    count = 0
    point = 0

    for i in str:
        if i == "O":
            count += 1
            point += count
        else:
            count = 0

    points.append(point)

for p in points:
    print(p)