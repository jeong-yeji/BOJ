wheels = [list(map(int, list(input()))) for _ in range(4)]

for _ in range(int(input())):
    n, d = map(int, input().split())
    directions = [0 for _ in range(4)]
    directions[n - 1] = d

    for i in range(n - 1, 4 - 1):
        if wheels[i][2] == wheels[i + 1][6]:
            break
        directions[i + 1] = -directions[i]
    for i in range(n - 1, 0, -1):
        if wheels[i][6] == wheels[i - 1][2]:
            break
        directions[i - 1] = -directions[i]

    for idx, direction in enumerate(directions):
        if direction == 1:  # 시계
            wheels[idx] = wheels[idx][-1:] + wheels[idx][:-1]
        elif direction == -1:  # 반시계
            wheels[idx] = wheels[idx][1:] + wheels[idx][:1]
            
print(sum(1 << i for i in range(4) if wheels[i][0] == 1))
