# https://programmers.co.kr/learn/courses/30/lessons/12925


def solution(s):
    try:
        return int(s)
    except:
        return -int(s[1:])


# 그냥 return int(s)만 써도 되나봄
# 파이썬이 숫자와 부호만 있는경우 자동으로 인식해서 바꿔줌

print(solution("1234"))
print(solution("-1234"))