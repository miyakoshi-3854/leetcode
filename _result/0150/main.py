"""
150. Evaluate Reverse Polish Notation

条件
tokenを処理して計算結果を返す。

思考
計算する仕組みは理解したけど、どこにstackを使うんだ？
末尾から取り出すってこと？

トークンを左から順に見る
数字ならstackに積む
記号なら stackから2つ取り出して計算して、結果をstackに戻す
最後にstackに残った値が答え

"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        symbols = ("+", "-", "*", "/")
        n_stack = []

        for t in tokens:
            if t in symbols:
                n = n_stack.pop()
                m = n_stack.pop()
                if t == "+":
                    n_stack.append(m + n)
                elif t == "-":
                    n_stack.append(m - n)
                elif t == "*":
                    n_stack.append(m * n)
                elif t == "/":
                    n_stack.append(int(m / n))
            else:
                n_stack.append(int(t))

        return n_stack.pop()
