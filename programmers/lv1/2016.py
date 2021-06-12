# https://programmers.co.kr/learn/courses/30/lessons/12901


def solution(a, b):
    # month = {
    #     1: 31,
    #     2: 29,
    #     3: 31,
    #     4: 30,
    #     5: 31,
    #     6: 30,
    #     7: 31,
    #     8: 31,
    #     9: 30,
    #     10: 31,
    #     11: 30,
    #     12: 31,
    # }
    # day = {0: "THU", 1: "FRI", 2: "SAT", 3: "SUN", 4: "MON", 5: "TUE", 6: "WED"}

    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]

    for i in range(1, a):
        b += month[i - 1]

    return day[b % 7]


print(solution(5, 24))