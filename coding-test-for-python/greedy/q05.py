# 볼링공 고르기
from itertools import combinations
from collections import Counter


def solution(n, m, balls):
    cnt = Counter(balls)
    answer = 0
    for i in range(1, 10):
        if cnt[i] != 0:
            for j in range(i + 1, 10):
                answer += cnt[i] * cnt[j]
    return answer

    # answer = 0
    # combi = combinations(balls, 2)
    # for c in combi:
    #     if balls[c[0] - 1] != balls[c[1] - 1]:
    #         answer += 1
    # return answer


print(solution(5, 3, [1, 3, 2, 3, 2]))
print(solution(8, 5, [1, 5, 4, 3, 2, 4, 5, 2]))
