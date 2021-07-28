# 시각


def time(hour):
    answer = 0
    for h in range(hour + 1):
        for m in range(60):
            for s in range(60):
                if "3" in str(h) + str(m) + str(s):
                    answer += 1
    return answer


print(time(5))