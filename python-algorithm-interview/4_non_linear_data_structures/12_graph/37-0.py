# subsets
import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)+1):
            res += list(itertools.combinations(nums, i))
        return res