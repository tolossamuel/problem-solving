# Problem: Design a Stack With Increment Operation - https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        self.add = []

    def push(self, x: int) -> None:
        if len(self.stack) == self.size:
            return
        self.stack.append(x)
        self.add.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        x, inc = self.stack.pop(), self.add.pop()
        if self.stack:
            self.add[-1] += inc
        return x + inc

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            if k > len(self.stack):
                self.add[-1] += val
            else:
                self.add[k - 1] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)