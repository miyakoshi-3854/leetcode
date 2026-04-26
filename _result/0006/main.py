class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 斜め部分はnumRows - 2 の数になる
        # 思いついたこと
        # 例えば numRows が4なら行数は、1, 2, 3, 4, 3, 2, 1, ...繰り返しのようになる。
        # これをストリングの長さ分のループで回す感じになるか？

        if numRows == 1:
            return s

        rows = [""] * numRows
        current_row = 0
        direction = 0

        for char in s:
            rows[current_row] += char

            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1

            current_row += direction

        return "".join(rows)
