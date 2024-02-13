def sol1():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        dist, cnt, mv = y - x, 0, 1
        while dist > 0:
            cnt += 1
            dist -= mv
            if cnt % 2 == 0:
                mv += 1
        print(cnt)


def sol2():
    for _ in range(int(input())):
        x, y = map(int, input().split())
        distance = y - x
        root = int(distance ** 0.5)
        if distance <= 3:
            print(distance)
        elif root ** 2 == distance:
            print(root * 2 - 1)
        elif root ** 2 + root < distance:
            print(root * 2 + 1)
        else:
            print(root * 2)
