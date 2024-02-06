for _ in range(int(input())):
    n = int(input())
    stocks = list(map(int, input().split()))
    stocks.reverse()
    answer, cur = 0, stocks[0]
    for i in range(1, n):
        if stocks[i] > cur:
            cur = stocks[i]
        else:
            answer += cur - stocks[i]
    print(answer)
