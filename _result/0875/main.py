"""
875. Koko Eating Bananas

条件
h時間後までにpiles全てのbananaを食べきる
できるだけゆっくり食べたい

思考
二分探索

どこに二分探索使うんだ？

ブルートフォースは、
piles全部足して、hで割って切り上げかな


"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            mid = (l + r) // 2
            t_sum = 0
            for pile in piles:
                t_sum += (pile + mid - 1) // mid

            if t_sum > h:
                l = mid + 1
            elif t_sum <= h:
                r = mid - 1

        return l
