# 숫자 카드 게임


def number_card(n, m, numlist):
    answer = []
    for num in numlist:
        answer.append(min(num))
    return max(answer)


print(number_card(3, 3, [[3, 1, 2], [4, 1, 4], [2, 2, 2]]))
print(number_card(2, 4, [[7, 3, 1, 8], [3, 3, 3, 4]]))