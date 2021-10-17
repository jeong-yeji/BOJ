# two pointer 방식
# brute force는 시간 초과


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 현재 값이 0을 초과한 경우, 뒤의 숫자와 합으로 0을 만들 수 없으므로 break
            if nums[i] > 0:
                break

            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:  # sum == 0
                    res.append([nums[i], nums[left], nums[right]])

                    # left, right 양 옆으로 동일한 값이 있는 경우
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 현재 합이 0이므로 한쪽만 이동해선 0을 만들 수 없음
                    left += 1
                    right -= 1

        return res
