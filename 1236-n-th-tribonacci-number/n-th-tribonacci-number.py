class Solution:
    def __init__(self):
        self.catch = {}
    def travel(self,n):
        if n == 1 or n == 2:
            return 1
        if n == 0:
            return 0
        if n in self.catch:
            return self.catch[n]
        result = self.travel(n-1) + self.travel(n-2) + self.travel(n-3)
        self.catch[n] = result
        return result

    def tribonacci(self, n: int) -> int:
        return self.travel(n)