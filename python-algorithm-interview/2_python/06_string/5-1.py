# group-anagrams
# collections.defaultdict 이용

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        # 존재하지 않는 키를 삽입하려고 하려면 KeyError가 발생
        # => defaultdict() : 에러가 나지 않도록 항상 default 생성
        anagrams = defaultdict(list)
        for str in strs:
            anagrams["".join(sorted(str))].append(str)
        return list(anagrams.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
