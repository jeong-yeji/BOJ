stack, answer = 0, 0
brackets = input().replace("()", "|")
for bracket in brackets:
    if bracket == "(":
        stack += 1
    elif bracket == "|":
        answer += stack
    else:
        stack -= 1
        answer += 1
print(answer)
