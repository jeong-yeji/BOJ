heights = list(int(input()) for _ in range(9))
heights.sort()
s = sum(heights)

for i in range(9):
    for j in range(i):
        curr = s - (heights[i] + heights[j])
        if curr == 100:
            del heights[i]
            del heights[j]
            for height in heights:
                print(height)
            exit()
