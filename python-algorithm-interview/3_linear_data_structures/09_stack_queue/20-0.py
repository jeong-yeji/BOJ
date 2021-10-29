# valid-parentheses


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i not in parentheses:
                stack.append(i)
            elif not stack or parentheses[i] != stack.pop():
                return False
        return len(stack) == 0
