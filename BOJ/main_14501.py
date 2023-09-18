n = int(input())
interviews = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def recur(day, price):
    global answer
    if day >= n:
        if day == n:
            answer = max(answer, price)
        return

    recur(day + interviews[day][0], price + interviews[day][1])
    recur(day + 1, price)


recur(0, 0)
print(answer)
