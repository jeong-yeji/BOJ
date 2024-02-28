import heapq
import sys

input = sys.stdin.readline
algorithms_dict, difficulties_dict, problems_dict = {}, {}, {}


class Algorithm:
    def __init__(self, num):
        self.num = num
        self.minh = []
        self.maxh = []

    def insert(self, p, l):
        heapq.heappush(self.minh, (l, p))
        heapq.heappush(self.maxh, (-l, -p))

    def find(self, x):
        if x > 0:
            while self.maxh and (
                    -self.maxh[0][1] not in problems_dict or
                    problems_dict[-self.maxh[0][1]] != (self.num, -self.maxh[0][0])
            ):
                heapq.heappop(self.maxh)
            if self.maxh:
                return list(map(lambda i: -i, self.maxh[0]))
        else:
            while self.minh and (
                    self.minh[0][1] not in problems_dict or
                    problems_dict[self.minh[0][1]] != (self.num, self.minh[0][0])
            ):
                heapq.heappop(self.minh)
            if self.minh:
                return self.minh[0]
        return []


class Difficulty:
    def __init__(self, num):
        self.num = num
        self.minh = []
        self.maxh = []

    def insert(self, p):
        heapq.heappush(self.minh, p)
        heapq.heappush(self.maxh, -p)

    def find(self, x):
        if x > 0:
            while self.minh and (
                    self.minh[0] not in problems_dict or
                    problems_dict[self.minh[0]][1] != self.num
            ):
                heapq.heappop(self.minh)
            if self.minh:
                return self.minh[0]
        else:
            while self.maxh and (
                    -self.maxh[0] not in problems_dict or
                    problems_dict[-self.maxh[0]][1] != self.num
            ):
                heapq.heappop(self.maxh)
            if self.maxh:
                return -self.maxh[0]
        return []


def add(p, l, g):
    if g not in algorithms_dict:
        algorithms_dict[g] = Algorithm(g)
    algorithms_dict[g].insert(p, l)

    if l not in difficulties_dict:
        difficulties_dict[l] = Difficulty(l)
    difficulties_dict[l].insert(p)

    problems_dict[p] = (g, l)


def solved(p):
    del problems_dict[p]


def recommend(g, x):
    return algorithms_dict[g].find(x)[1]


def recommend2(x):
    p = -1
    l = 0 if x == 1 else 101
    for g, algorithm in algorithms_dict.items():
        target = algorithm.find(x)
        if target:
            if x > 0:
                if target[0] > l:
                    l, p = target
                elif target[0] == l and target[1] > p:
                    p = target[1]
            else:
                if target[0] < l:
                    l, p = target
                elif target[0] == l and target[1] < p:
                    p = target[1]
    return p


def recommend3(x, l):
    if x == -1:
        l += x
    while 0 <= l <= 100:
        if l in difficulties_dict:
            target = difficulties_dict[l].find(x)
            if target:
                return target
        l += x
    return -1


for _ in range(int(input())):
    add(*map(int, input().split()))

for _ in range(int(input())):
    cmd, *args = input().split()
    args = map(int, args)
    if cmd == 'add':
        add(*args)
    elif cmd == 'solved':
        solved(*args)
    elif cmd == 'recommend':
        print(recommend(*args))
    elif cmd == 'recommend2':
        print(recommend2(*args))
    elif cmd == 'recommend3':
        print(recommend3(*args))
