# 거스름돈


def change(n):
    money = [500, 100, 50, 10]
    answer = 0

    for m in money:
        a, n = divmod(n, m)
        answer += a

    return answer


print(change(1260))