# https://programmers.co.kr/learn/courses/30/lessons/12973


def solution(s):

    stack = []

    for i in s:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        else:
            stack.pop()

    return int(stack == [])
    # return not(stack)


print(solution("baabaa"))
print(solution("cdcd"))
