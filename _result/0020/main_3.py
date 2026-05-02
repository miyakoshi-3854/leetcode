"""
20. Valid Parentheses

条件
sの括弧全部が閉じられているか

思考
stack使う
解き方忘れた
len(s) == 2n + 1だったら即return

open, closeのdictを作ってo(n)計算できるようにする

"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        b = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in b:
                if len(stack) > 0 and stack[-1] == b[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        else:
            return True
