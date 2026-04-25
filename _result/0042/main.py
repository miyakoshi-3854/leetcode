"""
42. Trapping Rain Water

条件
穴にどれだけ水がたまるかを判定しintで返却

l, rが距離が1以上
l, rと穴の高低差が1以上

思考
l, rの間がどういう状態なのかを見ていく必要がある気がする


"""
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0

        l_max, r_max = 0, 0
        l, r = 0, len(height) - 1
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            if height[l] < height[r]:
                water += min(l_max, r_max) - height[l]
                l += 1
            else:
                water += min(l_max, r_max) - height[r]
                r -= 1

        return water