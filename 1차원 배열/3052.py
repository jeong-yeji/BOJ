# 나머지
# 10개의 자연수(0<n<=1000)를 받아 42로 나눈 나머지 중 서로 다른 값의 개수 출력

# 1차 제출
number = [int(input()) for _ in range(10)]
remainder = [n % 42 for n in number]
count = []
for r in remainder:
    if r not in count:
        count.append(r)
print(len(count))

# 2차 제출
count = set([int(input()) % 42 for _ in range(10)])
print(len(count))