from collections import deque


def AC(p, n, nums):
    if p.count("D") > n:
        return -1

    numlist = deque()
    if n > 0:
        numlist = deque(list(map(int, nums.split(","))))

    flag = True
    for i in p:
        if i == "R":
            flag = not flag
        elif flag:
            numlist.popleft()
        else:
            numlist.pop()

    if not flag:
        numlist.reverse()

    return list(numlist)


for _ in range(int(input())):
    p = input().replace("RR", "")
    n = int(input())
    nums = input()[1:-1]

    output = AC(p, n, nums)

    if output == -1:
        print("error")
    else:
        print(f"[{','.join(map(str, output))}]")
