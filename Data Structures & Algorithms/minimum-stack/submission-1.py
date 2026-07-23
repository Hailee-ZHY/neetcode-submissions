class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        res = self.stack.pop()
        return res

    def top(self) -> int:
        res = self.stack[-1]
        return res

    def getMin(self) -> int:
        return min(self.stack)