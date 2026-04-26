"""
36. valid sudoku

条件:
数字 1~9
行に同じ数字が存在しない
列に同じ数字が存在しない
9つの3x3に同じ数字が存在しない

attention
都度変数にいれてたらメモリ爆発するから、一つのlistを使いまわして判定したらclear

think
出現key, 回数valueのdictを作って、もしvalueが1より大きくなった瞬間falseとかでいけるか？
→ 普通にlistでよさそう。

行:
list != set(list)を利用する

列:
同上

3x3:
先に3x3の要素を2重配列持っておく

"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = []

        # 行
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                else:
                    digits.append(board[i][j])
            if len(digits) != len(set(digits)):
                return False
            digits.clear()

        # 列
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                else:
                    digits.append(board[j][i])
            if len(digits) != len(set(digits)):
                return False
            digits.clear()

        # 3x3
        _3x3 = [[] for _ in range(len(board))]
        for i in range(len(board)):
            h = i // 3
            for j in range(len(board)):
                v = j // 3
                if board[i][j] == ".":
                    continue
                else:
                    _3x3[h * 3 + v].append(board[i][j])
        for i in range(len(board)):
            if len(_3x3[i]) != len(set(_3x3[i])):
                return False

        return True
