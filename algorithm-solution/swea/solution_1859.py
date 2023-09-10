for t in range(int(input())):
    n = int(input())
    prices = list(map(int, input().split()))
    profit = 0
    curr = -1
    for i in range(n - 1, -1, -1):
        if prices[i] > curr:
            curr = prices[i]
        else:
            profit += (curr - prices[i])
    print(f'#{t + 1} {profit}')
