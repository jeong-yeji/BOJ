# product-of-array-except-self
# Time Limitation : O(n)
# without using the division operation


class Solution:
    def productExceptSelf(self, nums):
        res = []

        # left
        product = 1
        for i in range(len(nums)):
            res.append(product)
            product *= nums[i]

        # right
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= product
            product *= nums[i]

        return res
