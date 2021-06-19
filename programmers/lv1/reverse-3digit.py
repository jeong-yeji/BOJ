# https://programmers.co.kr/learn/courses/30/lessons/68935


# def convert(n, base):
#     T = "0123456789ABCDEF"
#     q, r = divmod(n, base)
#     if q == 0:
#         return T[r]
#     else:
#         return convert(q, base) + T[r]


# def solution(n):
#     return int(convert(n, 3)[-1::-1], 3)


def solution(n):
    num = ""
    while n:
        num += str(n % 3)
        n = n // 3
    return int(num, 3)