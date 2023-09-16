h, w = map(int, input().split())
heights = list(map(int, input().split()))
answer = 0
for i in range(1, w - 1):
    left = max(heights[:i + 1])
    right = max(heights[i:])
    answer += abs(heights[i] - min(left, right))
print(answer)
