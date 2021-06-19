# https://programmers.co.kr/learn/courses/30/lessons/12935


def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]


print(solution([4, 3, 2, 1]))
print(solution([10]))