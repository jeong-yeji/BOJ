def count2(n):
    answer = n
    for i in range(1, 50):
        answer += (n // (2 ** i)) * (2 ** (i - 1))
    return answer


a, b = map(int, input().split())
print(count2(b) - count2(a - 1))
