"""
11. Container With Most Water

条件
距離 × 高さが一番の大きくなる組み合わせを探す

注意
sortしたら情報が失われる

思考
縦の大きさは[l], [r]の小さいほうの大きさ
横はr - lの数

全部計算して、大きければ上書きするみたいな感じか？

"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0

        l, r = 0, len(height) - 1
        while l < r:
            min_height = min(height[l], height[r])
            length = r - l
            max_water = max(max_water, min_height * length)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water