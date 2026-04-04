class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        matching = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in matching:
                stack.append(char)
            elif not stack or matching[stack[-1]] != char:
                return False
            else:
                stack.pop()

        return not stack