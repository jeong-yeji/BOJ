# https://programmers.co.kr/learn/courses/30/lessons/12945


def solution(n):
    # 1
    # fibo = [0, 1]
    # for i in range(2, n + 1):
    #     fibo.append(fibo[i - 1] + fibo[i - 2])
    # return fibo[n] % 1234567

    # 2
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b % 1234567


print(solution(100000))
print(solution(5))