class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        self._min = float("inf")
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min and self.min[-1] >= val:
            self.min.append(val)
        elif not self.min:
            self.min.append(val)
    def pop(self) -> None:
        x = self.stack.pop()
        if self.min and self.min[-1] == x:
            self.min.pop()
            

    def top(self) -> int:

        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()