# https://programmers.co.kr/learn/courses/30/lessons/12909

# 변수 두개 이용
# def solution(s):
#     open, close = 0, 0

#     for i in s:
#         if i == '(':
#             open += 1
#         else:
#             close += 1

#         if open < close:
#             return False

#     if open == close:
#         return True

#     return False


# 변수 한개 이용
def solution(s):
    bracket = 0

    for i in s:
        if i == "(":
            bracket += 1
        else:
            bracket -= 1

        if bracket < 0:
            return False

    if bracket == 0:
        return True

    return False


print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))