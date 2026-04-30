"""
76. Minimum Window Substring

条件
tのanaglam + αが存在する最小のwindowを返す

思考
長さが不定の尺取り法
びびらずfor rが右へ舐める

まず成り立つ条件は、
- tのanaglam + αがwindowに存在する

どんな条件のときに、lを詰めればいいか考える必要がある
→ window内のs[l]の個数 > tで必要なs[l]の個数のとき動かせる

window長さを最小にする
min(len(cur_window), len(window))

"""

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_d = defaultdict(int)
        for c in t:
            t_d[c] += 1

        window_d = defaultdict(int)
        min_window = ""
        l = 0
        for r in range(len(s)):
            window_d[s[r]] += 1
            while (
                all(window_d[c] >= t_d[c] for c in t_d) and window_d[s[l]] > t_d[s[l]]
            ):
                window_d[s[l]] -= 1
                l += 1

            if all(window_d[c] >= t_d[c] for c in t_d) and (
                min_window == "" or len(s[l : r + 1]) < len(min_window)
            ):
                min_window = s[l : r + 1]

        return min_window
