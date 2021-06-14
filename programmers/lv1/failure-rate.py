# https://programmers.co.kr/learn/courses/30/lessons/42889


from collections import Counter


def solution(N, stages):
    rates = {}
    cnt = Counter(stages)

    for i in range(1, N + 1):
        not_clear = cnt[i]
        clear = sum([cnt[j] for j in range(i, N + 2)])
        try:
            rate = not_clear / clear
        except:
            rate = 0
        rates[i] = rate

    rates = sorted(rates.items(), key=lambda x: x[1], reverse=True)

    return [rate[0] for rate in rates]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))