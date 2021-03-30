# 한수
# 어떤 양의 정수 x의 각 자리가 등차수열 -> 한수
# 등차수열 : 연속된  두 개의 수의 차이가 일정한 수열
# n이 주어졌을 때, 1 이상 n 이하인 한수의 개수 출력 (n<=1000)

# 방법 1
def ap1(n):
    if n < 100:  # 1-99는 모두 한수
        return n

    count = 99  # 1-99는 모두 한수

    for i in range(100, n + 1):
        i = str(i)
        dif = []

        for j in range(len(i) - 1):
            dif.append(int(i[j]) - int(i[j + 1]))
        # dif = [int(i[j]) - int(i[j + 1]) for j in range(len(i) - 1)]

        if len(set(dif)) == 1:
            count += 1

    return count


print(ap1(int(input())))


# 방법 2
def ap2(n):
    if n < 100:
        return n

    count = 99
    for i in range(100, n):
        a = list(map(int, str(i)))
        if a[0] - a[1] == a[1] - a[2]:
            count += 1

    return count


print(ap2(int(input())))