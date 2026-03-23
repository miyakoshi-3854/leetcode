class Solution:
    def myAtoi(self, s: str) -> int:
        # 一個ずつ条件書いていく感じか？
        # 思いついたこと
            # 一文字ずつ char として処理する

        # スペースを飛ばす
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        
        # 文字列の最後に到達していないか
        if i == len(s):
            return 0

        # 処理された後の文字が数字であるか
        if not s[i].isdigit() and s[i] != "+" and s[i] != "-":
            return 0

        # 符号チェック
        sign = 1
        if s[i] == "-":
            sign = - 1
            i += 1
        elif s[i] == "+":
            i += 1

        # 数字取得
        num = 0
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - 2 ** 31

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                if sign == 1:
                    return INT_MAX
                return INT_MIN
            
            num = num * 10 + digit
            i += 1

        num *= sign
        return num