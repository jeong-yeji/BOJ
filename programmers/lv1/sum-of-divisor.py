# https://programmers.co.kr/learn/courses/30/lessons/12928


def solution(n):
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += i
            if i != n // i:
                answer += n // i
    return answer


print(solution(12))
print(solution(5))
print(solution(16))