# https://programmers.co.kr/learn/courses/30/lessons/12912

# 등차수열의 합 공식 이용
def solution(a, b):
    return (abs(a - b) + 1) * (a + b) / 2


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))