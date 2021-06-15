# https://programmers.co.kr/learn/courses/30/lessons/12954


def solution(x, n):
    # 1
    return [x * i for i in range(1, n + 1)]

    # 2
    # answer = [x]
    # for _ in range(n-1):
    #     answer.append(answer[-1]+x)
    # return answer

    # 3: 이건 x=0일때 에러 발생 (ValueError: range() arg 3 must not be zero)
    # return list(range(x, x * (n + 1), x))


print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))
print(solution(0, 2))