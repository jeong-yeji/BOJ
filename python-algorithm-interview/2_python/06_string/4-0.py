# most-common-word

from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        words = re.sub(r"[^\w]", " ", paragraph).lower().split()
        res = [word for word in words if word not in banned]
        return Counter(res).most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))
paragraph = "a."
banned = []
print(Solution().mostCommonWord(paragraph, banned))
