# top-k-frequent-elements


import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnts = collections.Counter(nums).most_common(k)
        return [cnt[0] for cnt in cnts]
