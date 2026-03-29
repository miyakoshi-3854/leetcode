class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 回文だから、あるstringの頭とけつが同じであること
        # 一つのcharを選択して、stringの中に同じcharがあるかを探し、
        # どんどん内側に向けて一致していくかを探していくみたいな感じかな？
        # 思いついたこと    
            # listのindexのleftは左に拡張したいから-1、rightは右に拡張したいから+1になりそう
        result = ""
        resultLength = 0

        for i in range(len(s)):
            # 奇数
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLength:
                    result = s[left:right + 1]
                    resultLength = right - left + 1 
                left -= 1
                right += 1

            # 偶数
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resultLength:
                    result = s[left:right + 1]
                    resultLength = right - left + 1 
                left -= 1
                right += 1

        return result