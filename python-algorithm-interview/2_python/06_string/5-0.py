# group-anagrams


class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        for str in strs:
            k = "".join(sorted(str))
            if k in anagrams.keys():
                anagrams[k].append(str)
            else:
                anagrams[k] = [str]
        return list(anagrams.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
