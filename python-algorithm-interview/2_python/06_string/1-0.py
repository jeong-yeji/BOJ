import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
    
        return s == s[::-1]


s1 = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s1)) # True

s2 = "race a car"
print(Solution().isPalindrome(s2)) # False
