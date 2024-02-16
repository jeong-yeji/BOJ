import sys

input = lambda: sys.stdin.readline().strip()


def sol1(n, m, trees):
    s, e = 0, max(trees)
    while s < e:
        mid = (s + e + 1) // 2
        if sum(tree - mid for tree in trees if tree > mid) >= m:
            s = mid
        else:
            e = mid - 1
    return s


def sol2(n, m, trees):
    s, e = 1, max(trees)
    while s <= e:
        mid = (s + e) // 2
        cut = sum(tree - mid for tree in trees if tree > mid)
        if cut >= m:
            s = mid + 1
        else:
            e = mid - 1
    return e


def sol3(n, m, trees):  # fastest
    from collections import Counter
    counter = Counter(trees)
    s, e = 0, max(counter.keys())
    while s < e:
        mid = (s + e + 1) // 2
        if sum((h - mid) * i for h, i in counter.items() if h > mid) >= m:
            s = mid
        else:
            e = mid - 1
    return s


if __name__ == "__main__":
    n, m = map(int, input().split())
    trees = list(map(int, input().split()))
    # print(sol1(n, m, trees))
    # print(sol2(n, m, trees))
    print(sol3(n, m, trees))
