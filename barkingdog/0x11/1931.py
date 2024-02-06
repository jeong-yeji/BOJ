n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
meetings.sort(key=lambda x: (x[1], x[0]))
answer, t = 0, 0
for s, e in meetings:
    if t <= s:
        answer += 1
        t = e
print(answer)
