# 큰 수의 법칙


def large_number(n, m, k, num):
    num.sort(reverse=True)
    answer = (num[0] * k + num[1]) * (m // (k + 1)) + num[0] * (m % (k + 1))
    return answer


print(large_number(5, 8, 3, [2, 4, 5, 4, 6]))