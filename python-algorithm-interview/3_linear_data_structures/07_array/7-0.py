# two-sum


class Solution:
    def twoSum(self, nums, target: int):
        for idx, num in enumerate(nums):
            if target - num in nums[idx + 1 :]:
                return [idx, nums[idx + 1 :].index(target - num) + idx + 1]


print(Solution().twoSum(nums=[2, 7, 11, 15], target=9))  # [0,1]
print(Solution().twoSum(nums=[3, 2, 4], target=6))  # [1,2]
print(Solution().twoSum(nums=[3, 3], target=6))  # [0,1]
