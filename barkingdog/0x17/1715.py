import heapq
import sys

input = sys.stdin.readline
cards = []
for _ in range(int(input())):
    heapq.heappush(cards, int(input()))
answer = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    answer += a + b
    heapq.heappush(cards, a + b)
print(answer)
