h, w = map(int, input().split())
heights = list(map(int, input().split()))

answer = 0
left, right = 0, w - 1
max_left, max_right = heights[left], heights[right]

while left < right:
    max_left = max(max_left, heights[left])
    max_right = max(max_right, heights[right])

    if max_left >= max_right:
        answer += max_right - heights[right]
        right -= 1
    if max_left < max_right:
        answer += max_left - heights[left]
        left += 1
        
print(answer)
