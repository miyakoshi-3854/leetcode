"""
84. Largest Rectangle in Histogram

条件


思考
stack使う
減少傾向のmonotonic stackか？
→ 逆で増加傾向のmonotonic stack

なにこれ？どうすんの？
？？？

縦
以前見た数字よりも小さい値が来た瞬間、縦の大きさが更新される。

横
topよりも小さい値が来たら、四角形はもう大きくなれないので、
四角形の右端が確定する

"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for r in range(len(heights)):
            while stack and heights[r] < heights[stack[-1]]:
                h = heights[stack.pop()]
                l = stack[-1] if stack else -1
                max_area = max(max_area, h * (r - l - 1))
            else:
                stack.append(r)

        while stack:
            h = heights[stack.pop()]
            l = stack[-1] if stack else -1
            max_area = max(max_area, h * (len(heights) - l - 1))

        return max_area
