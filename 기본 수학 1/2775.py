# 부녀회장이 될테야
# 방법 1 : 재귀 - 시간 초과로 실패
def apartment(k, n):
    if k == 0:
        return n
    people = 0
    for i in range(1, n + 1):
        people += apartment(k - 1, i)
    return people


for _ in range(int(input())):
    k = int(input())
    n = int(input())
    print(apartment(k, n))


# 방법 2
for _ in range(int(input())):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n + 1)]  # 0층
    for _ in range(k):
        for i in range(1, n):
            people[i] += people[i - 1]
    print(people[-1])
