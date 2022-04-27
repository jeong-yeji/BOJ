# longest-substring-without-repeating-characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        for i in range(len(set(s)), 0, -1):
            if i == 1:
                return i

            for j in range(len(s) - i + 1):
                if len(set(s[j : j + i])) == i:
                    return i
