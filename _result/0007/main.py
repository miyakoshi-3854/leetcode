class Solution:
    def reverse(self, x: int) -> int:
        # 単純に先頭と末尾を相対的に入れ替えるだけでいいのかな？
        # いや、単純にひとつづつリストに入れて、後ろから取り出すだけでよさそう

        # 思いついたこと
        # 負の値は取り扱いずらそうなので、if x >= 0: みたいな正負のフラグを用意して最後に、正負を付けるのがよさそう！

        sign = 1

        if x < 0:
            sign = -1

        x = abs(x)

        res = 0

        while x != 0:
            digit = x % 10
            res = res * 10 + digit
            x //= 10

        res *= sign

        if res < -(2**31) or res > 2**31 - 1:
            return 0

        return res
