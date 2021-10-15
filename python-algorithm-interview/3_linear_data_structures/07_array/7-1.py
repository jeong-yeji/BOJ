# two-sum 다른 해결 법


class Solution:
    # 1. Brute Force : 가장 느림. O(n^2)
    def brute_force(self, nums, target: int):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # 2. in => 내가 사용한 방법 : O(n^2)으로 시간복잡도는 같지만 in이 더 빠름
    def using_in(self, nums, target: int):
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i + 1]:
                return [i, nums[i + 1 :].index(complement) + (i + 1)]

    # 3. 첫번째 수를 뺀 결과 키 조회 : 평균 O(1), 최악 O(n)
    def find_key_except_first_num_1(self, nums, target: int):
        # key <> value -> dict
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

    # 4. 3 구조 개선 : 성능의 차이는 없지만 코드가 간결해짐
    def find_key_except_first_num_2(self, nums, target: int):
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i

    # 만약 정렬된 리스트라면 투 포인터 방식을 이용해도 됨
    # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
    # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
    # 합이 타겟과 같으면 return
