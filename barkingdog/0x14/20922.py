from collections import defaultdict


def sol1(n, k, numbers):  # 400ms
    limit = defaultdict(list)
    s = ans = 0
    for e in range(n):
        while limit[numbers[e]] and limit[numbers[e]][0] < s:
            limit[numbers[e]].pop(0)
        limit[numbers[e]].append(e)
        if len(limit[numbers[e]]) > k:
            s = limit[numbers[e]][0] + 1
        ans = max(ans, e - s + 1)
    return ans


def sol2():  # 216ms
    cnt_list = [0] * 100001
    s = ans = 0
    for e in range(n):
        cnt_list[numbers[e]] += 1
        while cnt_list[numbers[e]] > k:
            cnt_list[numbers[s]] -= 1
            s += 1
        ans = max(ans, e - s + 1)
    return ans


if __name__ == "__main__":
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(sol1(n, k, numbers))
