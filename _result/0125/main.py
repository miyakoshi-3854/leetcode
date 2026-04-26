"""
125. valid palindrome

条件
小文字アルファベットにサニタイズ
sが回文かどうか
boolを返す

どうやってサニタイズするんだ？
pythonは便利な関数ありそうだな。
→ re という標準ライブラリがある

two pointerね
文頭、文末にイテラブルを用意

"""

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitized = re.sub(r"[^a-z0-9]", "", s.lower())

        l, r = 0, len(sanitized) - 1
        while l < r:
            if sanitized[l] == sanitized[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
