# https://programmers.co.kr/learn/courses/30/lessons/12921


def solution(n):
    nums = set(range(2, n + 1))
    non_prime = set()

    for i in range(2, int(n ** 0.5) + 1):
        for j in range(2, n // i + 1):
            non_prime.add(i * j)

    return len(nums - non_prime)


print(solution(10))
print(solution(5))