class Solution:
    def __init__(self):
        self.pos = set()
        self.col = set()
        self.neg = set()
        self.board = []
        self.ans = []
    def travel(self,row):
        if row  == len(self.board):
            copy = ["".join(i) for i in self.board]
            self.ans.append(copy)
            return 
        for i in range(len(self.board)):
            if i in self.col or (i+row) in self.pos or (row - i) in self.neg:
                continue
            self.pos.add(i+row)
            self.neg.add(row-i)
            self.col.add(i)
            self.board[row][i] ="Q"
            self.travel(row + 1)
            self.pos.remove(i+row)
            self.neg.remove(row-i)
            self.col.remove(i)
            self.board[row][i] = "."
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [["." for _ in range(n)] for _ in range(n)]
        self.travel(0)
       
        return self.ans