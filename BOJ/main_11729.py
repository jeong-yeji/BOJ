# 하노이 탑 이동 순서
def hanoitop(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoitop(n - 1, start, 6 - start - end)
    print(start, end)
    hanoitop(n - 1, 6 - start - end, end)


n = int(input())
print(2 ** n - 1)
hanoitop(n, 1, 3)

# 원판은 1, 2, 3으로 합이 6이므로 start, end를 알면 나머지 원판이 뭔지 알 수 있음