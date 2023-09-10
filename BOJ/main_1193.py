# 분수 찾기
x = int(input())
a = 0
n = 1

while a < x:
    a += n
    n += 1

dif = a - x + 1
if n % 2 == 1:
    print(f"{n-dif}/{dif}")
else:
    print(f"{dif}/{n-dif}")
