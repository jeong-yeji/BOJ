# 왕실의 나이트


def knight(pos):
    answer = 0
    x = int(pos[1])
    y = ord(pos[0]) - 96
    steps = [[-2, 1], [-2, -1], [2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

    for step in steps:
        nx = x + step[0]
        ny = y + step[1]
        if 1 <= nx <= 8 and 1 <= ny <= 8:
            answer += 1

    return answer


print(knight("a1"))
print(knight("c2"))
