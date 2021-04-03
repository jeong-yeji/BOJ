# 별 찍기 - 10
def drawStar(n):
    starlist = []
    l = len(n)
    for i in range(3 * l):
        idx = i % l
        if i // l == 1:
            starlist.append(n[idx] + " " * l + n[idx])
        else:
            starlist.append(n[idx] * 3)
    return starlist


star = ["***", "* *", "***"]
num = [3 ** i for i in range(1, 8)]

for _ in range(num.index(int(input()))):
    star = drawStar(star)

for s in star:
    print(s)