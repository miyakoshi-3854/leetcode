"""
424. Longest Repeating Character Replacement

条件
k回何かを置き換える
同じ文字からなる一番長い文字列を作る

思考
sliding window使うんだよね
とりあえず左から右に舐める

今見ている文字が何連続かを数えていく
もし今見ている文字を置き換えたときに何連続になるか記録？
max()で更新？

解説後
lポインタの動きの意味がわからんな

"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        left = 0
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res
