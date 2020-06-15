"""
对原栈和辅助栈的处理过程如下：

元素压入原栈的时候，如果辅助栈为空，或者元素 <= 辅助栈的栈顶元素，那么将元素也压入辅助栈
元素弹出原栈的时候，如果元素等于辅助栈的栈顶元素，辅助栈也弹出元素
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self) -> None:
        tmp = self.stack.pop()
        if tmp == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.min())
obj.pop()
param_3 = obj.top()
print(param_3)
param_4 = obj.min()
print(param_4)
