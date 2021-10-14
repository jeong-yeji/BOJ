# longest-palindromic-substring


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투포인터 확장
        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1 : right]

        # 해당 사항 없을 때는 바로 반환
        if len(s) < 2 or s == s[::-1]:
            return s

        res = ""
        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            res = max(res, expand(i, i + 1), expand(i, i + 2), key=len)
        return res


print(Solution().longestPalindrome("babad"))  # bab이나 aba도 가능
print(Solution().longestPalindrome("cbbd"))  # bb
print(Solution().longestPalindrome("a"))  # a
print(Solution().longestPalindrome("ac"))  # a
