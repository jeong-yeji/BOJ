# https://programmers.co.kr/learn/courses/30/lessons/12911


def solution(n):
    n_1 = bin(n).count("1")

    while True:
        n += 1
        if n_1 == bin(n).count("1"):
            return n


print(solution(78))
print(solution(15))