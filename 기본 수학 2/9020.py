# 골드바흐의 추측
# 소수 판별 리스트
n = 10000
num_list = [True] * n
for i in range(2, int(n ** 0.5) + 1):
    if num_list[i]:
        for j in range(2 * i, n, i):
            num_list[j] = False


# 1차
for _ in range(int(input())):
    n = int(input()) // 2
    if num_list[n]:
        print(n, n)
    else:
        i = 1
        while True:
            if num_list[n - i] and num_list[n + i]:
                print(n - i, n + i)


# 2차
for _ in range(int(input())):
    n = int(input()) // 2
    i = 0
    if num_list[n]:
        pass
    else:
        while True:
            i += 1
            if num_list[n - i] and num_list[n + i]:
                break
    print(n - i, n + i)


# 3차
for _ in range(int(input())):
    n = int(input()) // 2
    i = 0
    while True:
        if num_list[n - i] and num_list[n + i]:
            break
        i += 1
    print(n - i, n + i)


# 4차
for _ in range(int(input())):
    n = int(input()) // 2
    i = 0
    while not (num_list[n - i] and num_list[n + i]):
        i += 1
    print(n - i, n + i)