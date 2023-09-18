n = int(input())
ingredients = [list(map(int, input().split())) for _ in range(n)]
answer = 999_999_999


def curr(cnt, sour, bitter, used):
    if cnt == n:
        if used:
            global answer
            answer = min(answer, abs(sour - bitter))
        return

    curr(cnt + 1, sour * ingredients[cnt][0], bitter + ingredients[cnt][1], True)
    curr(cnt + 1, sour, bitter, used)


curr(0, 1, 0, False)

print(answer)
