"""
74. Search a 2D Matrix

条件
matrixの中からtargetを探す
存在するかをboolで返す

思考
二分探索

[m][0] <= target <= [m][- 1]
これが成り立つのか探してから、[m][n]を探索する
二分探索は[m][n]を探索する段階からでいいのか？
[m]を探す時点から二分探索するのか？
→ そうっぽい

target < [mid][0] → 上の行へ
target > [mid][-1] → 下の行へ
[mid][0] <= target <= [mid][-1] → その行で列を二分探索


"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
