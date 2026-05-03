"""
155. Min Stack

条件
stackの関数を自作する？
o(1)

思考
push append()
pop pop()
top なにこれ先頭返すだけ？
getMin min()はo(n)だから使えないな。

o(1)と言われたら、dict, setという直感

"""


class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)

        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        elif val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.main_stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()

        self.main_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
