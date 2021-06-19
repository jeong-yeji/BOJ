# https://programmers.co.kr/learn/courses/30/lessons/67256


def solution(numbers, hand):
    key_dict = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        "*": (3, 0),
        0: (3, 1),
        "#": (3, 2),
    }

    answer = ""

    lp = "*"
    rp = "#"

    for num in numbers:
        b = ""

        if num in [1, 4, 7]:
            b = "left"
        elif num in [3, 6, 9]:
            b = "right"
        else:
            curr = key_dict[num]
            left = key_dict[lp]
            right = key_dict[rp]

            leftD = abs(curr[0] - left[0]) + abs(curr[1] - left[1])
            rightD = abs(curr[0] - right[0]) + abs(curr[1] - right[1])

            if rightD < leftD:
                b = "right"
            elif rightD > leftD:
                b = "left"
            elif leftD == rightD:
                b = hand

        if b == "right":
            answer += "R"
            rp = num
        else:
            answer += "L"
            lp = num

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))