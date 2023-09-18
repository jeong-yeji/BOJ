n = int(input())
mp, mf, ms, mv = map(int, input().split())
ingredients = [list(map(int, input().split())) for _ in range(n)]
answer_price, answer_arr = 999_999_999, []


def recur(cnt, cp, cf, cs, cv, cm, arr):
    if cp >= mp and cf >= mf and cs >= ms and cv >= mv:
        global answer_price, answer_arr
        if cm < answer_price:
            answer_price = cm
            answer_arr = arr[:]
        return

    if cnt == n:
        return

    p, f, s, v, m = ingredients[cnt]
    arr.append(cnt + 1)
    recur(cnt + 1, cp + p, cf + f, cs + s, cv + v, cm + m, arr)
    arr.pop()
    recur(cnt + 1, cp, cf, cs, cv, cm, arr)


recur(0, 0, 0, 0, 0, 0, [])

if answer_price == 999_999_999:
    print(-1)
else:
    print(answer_price)
    print(*answer_arr)
