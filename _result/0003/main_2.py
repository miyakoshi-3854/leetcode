"""
3. Longest Substring Without Repeating Characters

条件
左から右に舐める
sの中から重複しない最大の文字列を探す

思考
見たものをdictに入れて、o(n)で検索できるようにするのが賢そう
重複したら、長さを数えてlength変数に大きい方を入れ替える。
dictをclear()
→ 重複した瞬間に消すと、1つ足りなくなる？からダメだ
→→ two pointerで重複するまで足すみたいな感じかな

最後まで見たら終わりかな

"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        d = {}
        result = 0

        for r in range(len(s)):
            if s[r] in d:
                while l <= d[s[r]]:
                    del d[s[l]]
                    l += 1

            d[s[r]] = r
            result = max(result, r - l + 1)

        return result
