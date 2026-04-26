"""
o(n log n)だからソート(tim sort)は禁止かな
別にする意味無くね？

dict(hash)でnumsの要素をkeyに出現回数をvalueにしてカウントしていく感じかな
それでdict[:k]個分からreturnすれば行けそう

いや待て、どうやって最頻する値を順番に大きい順からk個取り出すんだ？
sort出来ないぞ
別に順番とかじゃなくて大きいものをk個探せばいいんじゃね

heap使えそう
だけど、計算量がオーバーしないかな？どうだろう
valueが大きいもののkeyをかえしたいけど、指定の仕方がわからん

outputがlistの中に入る形になってるな
"""


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in d.items():
            bucket[count].append(num)

        ans = []
        for i in range(len(bucket) - 1, 0, -1):
            ans.extend(bucket[i])
            if len(ans) >= k:
                break

        return ans[:k]
