"""
128. longest consecutive sequence

条件
o(n)
0以上10**5以下
連続する整数の長さはどのくらいか

思考
そもそも重複は絶対にいらないからset()でいいはず

一番小さい数字はmin()で取る o(n)
→ minが一番長いとは限らないか

iterable in nums が成立する間のカウントを[]とかで記憶
後でmax()で取り出すとか？



"""
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if (n - 1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)

        return longest