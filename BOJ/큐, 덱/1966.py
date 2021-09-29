# 프린터 큐
for _ in range(int(input())):
    n, m = map(int, input().split())
    importance = list(map(int, input().split()))
    idxlist = [False for _ in range(n)]
    idxlist[m] = True
    cnt = 0

    while True:
        if importance[0] == max(importance):
            cnt += 1

            if idxlist[0]:
                print(cnt)
                break

        else:
            importance.append(importance[0])
            idxlist.append(idxlist[0])

        del importance[0]
        del idxlist[0]
