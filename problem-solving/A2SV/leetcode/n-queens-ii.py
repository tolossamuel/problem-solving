class Solution:
    def __init__(self):
        self.col = set()
        self.pos = set()
        self.neg = set()
        self.ans = 0
        self.board = []
    def travel(self,row):
        if row == len(self.board):
            self.ans += 1
            return 
        for i in range(len(self.board)):
            if i in self.col or (row + i) in self.pos or (row - i) in self.neg:
                continue
            self.col.add(i)
            self.pos.add(i+row)
            self.neg.add(row - i)
            self.travel(row + 1)
            self.col.remove(i)
            self.pos.remove(i+ row)
            self.neg.remove(row - i)
    def totalNQueens(self, n: int) -> int:
        self.board = [["." for _ in range(n)] for _ in range(n)]
        self.travel(0)
        return self.ans