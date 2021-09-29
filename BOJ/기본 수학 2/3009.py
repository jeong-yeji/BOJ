# 네번째 점
xpoints = []
ypoints = []

for _ in range(3):
    x, y = map(int, input().split())
    xpoints.append(x)
    ypoints.append(y)

# if xpoints[0] == xpoints[1]:
#     print(xpoints[2], end=" ")
# elif xpoints[0] == xpoints[2]:
#     print(xpoints[1], end=" ")
# else:
#     print(xpoints[0], end=" ")

# if ypoints[0] == ypoints[1]:
#     print(ypoints[2])
# elif ypoints[0] == ypoints[2]:
#     print(ypoints[1])
# else:
#     print(ypoints[0])

for i in range(3):
    if xpoints.count(xpoints[i]) == 1:
        x = xpoints[i]
    if ypoints.count(ypoints[i]) == 1:
        y = ypoints[i]

print(x, y)
