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
        rows = [set() for _ in range(len(board))]
        cols = [set() for _ in range(len(board))]
        boxes = [set() for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val == ".":
                    continue

                box_idx = (i // 3) * 3 + (j // 3)
                if val in rows[i] or val in cols[j] or val in boxes[box_idx]:
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[box_idx].add(val)

        return True
