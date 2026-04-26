class Solution:
    def isPalindrome(self, x: int) -> bool:
        # xから一桁目を抜き取って、抜き取った順でnumに代入していく感じか？
        # そしてx = numならtrue違うならfalseでいいか？
        # エッジケースは、負の数の時で、早期リターンすればいいかな？

        if x < 0:
            return False

        if x % 10 == 0 and x != 0:
            return False

        originalX = x
        num = 0
        while x != 0:
            digit = x % 10
            num = num * 10 + digit
            x //= 10

        return originalX == num
