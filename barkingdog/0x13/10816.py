def sol1():
    from collections import Counter

    n = int(input())
    cards = Counter(input().split())
    m = int(input())
    for target in input().split():
        val = cards.get(target)
        print(val if val else 0, end=' ')


def sol2():
    from collections import defaultdict

    n = int(input())
    counter = defaultdict(int)
    for card in input().split():
        counter[card] += 1
    m = int(input())
    for target in input().split():
        print(counter[target], end=' ')


def sol3():
    import bisect

    n = int(input())
    cards = list(map(int, input().split()))
    cards.sort()
    m = int(input())
    for target in map(int, input().split()):
        print(bisect.bisect_right(cards, target) - bisect.bisect_left(cards, target), end=' ')


def sol4():
    n = int(input())
    cards = list(map(int, input().split()))
    cards.sort()

    m = int(input())
    for target in map(int, input().split()):
        s, e = 0, n
        while s < e:
            mid = (s + e) // 2
            if cards[mid] > target:
                e = mid
            else:
                s = mid + 1
        upper = s

        s, e = 0, n
        while s < e:
            mid = (s + e) // 2
            if cards[mid] >= target:
                e = mid
            else:
                s = mid + 1
        lower = s

        print(upper - lower, end=' ')


if __name__ == "__main__":
    sol4()
