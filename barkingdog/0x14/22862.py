import sys

input = sys.stdin.readline


def sol1(n, k, numbers):
    e = ans = odd = even = 0
    for s in range(n):
        while odd <= k and e < n:
            if numbers[e] % 2:
                odd += 1
            else:
                even += 1

            if s == 0 and e == n:
                ans = even
                break

            e += 1

        if even > ans:
            ans = even

        if numbers[s] % 2:
            odd -= 1
        else:
            even -= 1

    return ans


def sol2(n, k, numbers):
    even = [0]  # 짝수의 개수 저장
    for number in numbers:
        if number % 2:
            even.append(even[-1])
        else:
            even[-1] += 1
        print(number, even)
    ans = even[:k + 1][-1]  # even[k]로 하면 arr가 k+1보다 작은 경우에 IndexError
    for i in range(len(even) - (k + 1)):
        ans = max(ans, even[i + k + 1] - even[i])
    return ans


if __name__ == "__main__":
    n, k = map(int, input().rstrip().split())
    numbers = list(map(int, input().rstrip().split()))
    print(sol1(n, k, numbers))
    print(sol2(n, k, numbers))
