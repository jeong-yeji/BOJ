def checkString(target, l):
    curr_list = []
    for i in range(0, l * (len(target) // l), l):
        curr_list.append(target[i: i + l])
        if i != 0:
            if curr_list[-1] != curr_list[-2]:
                return False
    return True


for t in range(int(input())):
    target = input().rstrip()
    res = 0
    for j in range(1, 11):
        if checkString(target, j):
            res = j
            break

    print(f'#{t + 1} {res}')
