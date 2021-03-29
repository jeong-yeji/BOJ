# 더하기 사이클

# 1차 제출
n = input().zfill(2)  # 빈 칸을 0으로 채워 두자리로 만듦
count = 0
new = n

while True:
    count += 1
    a = int(new[0])
    b = int(new[1])
    sum = str(a + b)
    new = str(b) + sum[len(sum) - 1]
    if n == new:
        break

print(count)

# 2차 제출
n = int(input())
count = 0
new = n

while True:
    count += 1
    a = new // 10
    b = new % 10
    new = b * 10 + (a + b) % 10
    # new = (new%10)*10 + ((new//10)+(new%10))%10
    if n == new:
        break

print(count)