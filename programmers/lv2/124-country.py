# https://programmers.co.kr/learn/courses/30/lessons/12899


# def solution(n):
#     answer = ""
#     while n > 0:
#         n -= 1
#         answer += "124"[n % 3]
#         n //= 3
#     return answer[::-1]


def solution(n):
    answer = ""
    while n > 0:
        n, a = divmod(n - 1, 3)
        answer = "124"[a] + answer
    return answer


print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))