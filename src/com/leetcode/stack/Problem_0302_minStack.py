"""
每当入栈的数小于等于栈顶元素时，随主栈都进行一次 push 操作；
当出栈的数与最小栈的栈顶元素相等时，最小栈也随主栈进行一次 pop 操作。
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
