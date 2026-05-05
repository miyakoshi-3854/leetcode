"""
739. Daily Temperatures

条件
前見た数字よりも大きい数字が来るまでに進んだ距離を返す

思考
stack

今見たindexにより小さいvalueを持つindexが無いかを調査して、
小さいものがあれば、解決するという感じか

"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [0]
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                result[j] = i - j
            else:
                stack.append(i)

        return result
