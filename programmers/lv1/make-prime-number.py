# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations


def solution(nums):
    # 소수 집합 생성
    n = min(sum(nums), 3000)
    non_prime = set([1])
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(2, n // i + 1):
            non_prime.add(i * j)

    answer = 0
    for num in combinations(nums, 3):
        if sum(num) not in non_prime:
            answer += 1

        # 소수 집합 만들지 않고 매번 검사하기 (for-else)
        # 느리지만... 이런것도 있다
        # s = sum(num)
        # for i in range(2, s):
        #     if s % i == 0:
        #         break
        # else:
        #     answer += 1

    return answer


print(solution([1, 2, 3, 4]))
print(solution([1, 2, 7, 6, 4]))
