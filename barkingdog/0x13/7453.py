import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ab, cd = [], []
for i in range(n):
    for j in range(n):
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])
ab.sort()
cd.sort()

i, j, answer = 0, len(cd) - 1, 0
while i < len(ab) and j >= 0:
    if ab[i] + cd[j] < 0:
        i += 1
    elif ab[i] + cd[j] > 0:
        j -= 1
    else:
        ni, nj = i + 1, j - 1

        while ni < len(ab) and ab[i] == ab[ni]:
            ni += 1

        while nj >= 0 and cd[j] == cd[nj]:
            nj -= 1

        answer += (ni - i) * (j - nj)
        i, j = ni, nj

print(answer)
