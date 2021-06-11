# https://programmers.co.kr/learn/courses/30/lessons/1845


def solution(nums):

    return min(len(nums) / 2, len(set(nums)))

    # l = len(nums)
    # s = len(set(nums))

    # if s > l / 2:
    #     return l / 2
    # else:
    #     return s
