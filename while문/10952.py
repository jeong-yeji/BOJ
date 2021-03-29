# A + B
# 0 0이 들어올 때까지 A+B
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)
