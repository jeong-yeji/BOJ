# jewels-and-stones


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        each_stone = [stone for stone in stones]
        cnt = 0
        for stone in each_stone:
            if stone in jewels:
                cnt += 1
        return cnt

        # return sum(stone in jewels for stone in stones)
