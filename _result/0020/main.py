class Solution:
    def isValid(self, s: str) -> bool:
        open_bracket = (
            "(",
            "[",
            "{",
        )
        close_bracket = (
            ")",
            "]",
            "}",
        )

        if len(s) % 2 == 1:
            return False

        stack = []
        for char in s:
            if char in open_bracket:
                stack.append(char)
                continue

            if not stack and char in close_bracket:
                return False
            elif open_bracket.index(stack[-1]) == close_bracket.index(char):
                stack.pop()
                continue
            else:
                return False

        return not stack
