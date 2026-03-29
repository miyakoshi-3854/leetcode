class Solution:
    def maxArea(self, height: List[int]) -> int:
        # ある線とある線で高さが低い方の高さ × 線と線の距離を求める問題
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            current_water = min(height[left], height[right]) * (right - left)
            max_water = max(max_water, current_water)

            # 高さが低い方方のポインタを真ん中へ動かす
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water