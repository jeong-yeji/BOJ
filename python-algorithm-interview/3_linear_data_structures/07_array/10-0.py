# array-partition-i


class Solution:
    # min() of each pair should be as large as possible
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        return sum(nums[::2])


print(Solution().arrayPairSum([1, 4, 3, 2]))  # 4
print(Solution().arrayPairSum([6, 2, 6, 5, 1, 2]))  # 9
