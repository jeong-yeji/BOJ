# 1이 될 때까지


def until_one(n, k):
    answer = 0
    while n != 1:
        answer += 1
        if n % k == 0:
            n //= k
        else:
            n -= 1
    return answer


print(until_one(25, 5))
print(until_one(27, 3))
print(until_one(17, 4))