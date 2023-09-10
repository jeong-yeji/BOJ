# AC
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def AC(p, n, nums):
    if p.count("D") > n:
        return -1

    numlist = deque([])
    if nums:
        numlist = deque(list(map(int, nums.split(","))))

    flag = 0
    for i in p:
        if i == "R":
            flag = not flag
        elif flag:
            numlist.pop()
        else:
            numlist.popleft()

    if flag:
        numlist.reverse()

    return list(numlist)


def printAC(numlist):
    for num in numlist[:-1]:
        print(num, end=",")
    print(numlist[-1], end="")


t = int(input())
for _ in range(t):
    p = input().replace("RR", "")
    n = int(input())
    nums = input()[1:-1]

    output = AC(p, n, nums)

    if output == -1:
        print("error")
    else:
        print("[", end="")
        if output:
            printAC(output)
        print("]")
