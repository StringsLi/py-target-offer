class TripleInOne:
    def __init__(self, stackSize: int):
        self.stackSize = stackSize
        self.array = stackSize * 3 * [0]
        self.st = [0, stackSize, 2 * stackSize]

    def push(self, stackNum: int, value: int) -> None:
        if self.st[stackNum] >= (stackNum + 1) * self.stackSize:
            return
        self.array[self.st[stackNum]] = value
        self.st[stackNum] += 1

    def pop(self, stackNum: int) -> int:
        if self.st[stackNum] == stackNum * self.stackSize:
            return -1
        r = self.array[self.st[stackNum] - 1]
        self.st[stackNum] -= 1
        return r

    def peek(self, stackNum: int) -> int:

        if self.st[stackNum] == stackNum * self.stackSize:
            return -1

        return self.array[self.st[stackNum] - 1]

    def isEmpty(self, stackNum: int) -> bool:
        return self.st[stackNum] == stackNum * self.stackSize