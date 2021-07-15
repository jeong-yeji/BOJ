# 괄호 변환


def isCorrect(p):
    bracket = 0

    for i in p:
        if i == "(":
            bracket += 1
        else:
            bracket -= 1

        if bracket < 0:
            return False

    return True


correct = ""


def solution(p):
    if p == "" or isCorrect(p):
        return p

    while True:
        u = p[0]
        v = ""
        for i in range(1, len(p)):
            u += p[i]
            if u.count("(") == u.count(")"):
                if i + 1 < len(p):
                    v = p[i + 1 :]
                break
        if isCorrect(u):
            global correct
            correct += u
            p = v
        else:
            answer = ""
            for i in u[1:-1]:
                if i == "(":
                    answer += ")"
                else:
                    answer += "("
            return correct + "(" + solution(v) + ")" + answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))