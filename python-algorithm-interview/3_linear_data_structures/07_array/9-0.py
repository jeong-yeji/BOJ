# 3Sum
# combinations를 이용하여 풀었으나 시간 초과로 실패

from itertools import combinations


class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        res = []
        for combi in list(combinations(nums, 3)):
            if sum(combi) == 0:
                c = sorted(combi)
                if c not in res:
                    res.append(c)

        return res


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
print(Solution().threeSum([]))  # []
print(Solution().threeSum([0]))  # []
