result = ["E", "A", "B", "C", "D"]
for _ in range(3):
    numbers = list(map(int, input().split()))
    cnt = numbers.count(0)
    print(result[cnt])
