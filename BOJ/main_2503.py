n = int(input())

hints = [input().split() for _ in range(n)]

answer = 0

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a == b or b == c or c == a:
                continue

            cnt = 0

            for hint in hints:
                target = list(map(int, str(hint[0])))
                strike = int(hint[1])
                ball = int(hint[2])

                strike_cnt = 0
                ball_cnt = 0

                if a in target:
                    if a == target[0]:
                        strike_cnt += 1
                    else:
                        ball_cnt += 1
                if b in target:
                    if b == target[1]:
                        strike_cnt += 1
                    else:
                        ball_cnt += 1
                if c in target:
                    if c == target[2]:
                        strike_cnt += 1
                    else:
                        ball_cnt += 1

                if ball == ball_cnt and strike == strike_cnt:
                    cnt += 1

            if cnt == n:
                answer += 1

print(answer)
