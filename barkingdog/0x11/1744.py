n = int(input())
numbers = [int(input()) for _ in range(n)]

plus, minus, zero, answer = [], [], False, 0
for number in numbers:
    if number == 1:
        answer += 1
    elif number > 0:
        plus.append(number)
    elif number < 0:
        minus.append(number)
    else:
        zero = True

plus.sort(reverse=True)
for i in range(0, len(plus), 2):
    if i + 1 >= len(plus):
        answer += plus[i]
    else:
        answer += plus[i] * plus[i + 1]

minus.sort()
for i in range(0, len(minus), 2):
    if i + 1 >= len(minus):
        if not zero:
            answer += minus[i]
    else:
        answer += minus[i] * minus[i + 1]

print(answer)
