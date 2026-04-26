"""
15. 3Sum

条件
3つの組み合わせが0になるものを全部探す
[]で返す

これ解き方覚えている気がする

two pointer使いたいからsortするという考えってあってんのかな？
sortしたら大きく、小さくを操作できるんだよね

メモリ制限が超過してしまった。どうしよう

"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1

        return result
