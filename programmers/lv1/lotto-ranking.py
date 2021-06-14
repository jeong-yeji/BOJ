# https://programmers.co.kr/learn/courses/30/lessons/77484


def solution(lottos, win_nums):
    ranking = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    # ranking = [6, 6, 5, 4, 3, 2, 1]
    count0 = lottos.count(0)
    intersect = len(set(lottos) & set(win_nums))
    return [ranking[intersect + count0], ranking[intersect]]