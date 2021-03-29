# A + B
# EOF. 입력이 끝날 때까지
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:  # 정수가 아닌 값이 들어왔을 때
        break
