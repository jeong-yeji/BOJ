# 문자열 반복
for _ in range(int(input())):
    r, s = map(str, input().split())
    r = int(r)
    for i in s:
        print(i * r, end="")
    print()
