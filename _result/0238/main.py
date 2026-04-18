"""
constraints
o(n)

todo
nums[i]以外のnums[]を全部掛け算する
[]に入れて返す

attention
pop(i)したらpop()がo(n)だからpop()した時点で終わってしまうな
2重forでnums[i]を回して、i以外の積を掛け算って感じも無理かな

think
繰り返しnums[i]以外の積を求めたいので再帰とか？
pythonの[i:j]みたいなのをうまく使えばiを除外できそうじゃない？

"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1] * n
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]

        r = [1] * n
        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]

        return [l[i] * r[i] for i in range(n)]
