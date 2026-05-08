"""
704. Binary Search

条件
o(log n)で計算しないといけない

思考
二分探索
二つに分けて探索で二分探索なんでしょ？

真ん中からみて、左右どっちにあるかを繰り返すやつだと思う

割った長さを先頭または、末尾として使って、
それ以前、それ以降をまた二分探索の範囲として使うんだと思う

10 ^ ? のときに二分探索が必要なんだ？

二つに分けるって言っても、確認する値は1つだから、偶数の時は小数点以下を考慮する必要あるか？

いつ終了するんだ？

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return -1
