class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = defaultdict(set)
        col = defaultdict(set)
        cells = defaultdict(set)
        search = []
        for i in range(9):
            for y in range(9):
                if board[i][y] != ".":
                    col[y].add(board[i][y])
                    row[i].add(board[i][y])
                    left = (y//3)
                    down = i//3
                    down = (down * 3) + 1
                    down += left
                    cells[down].add(board[i][y])
                else:
                    search.append([i,y])
        self.check = False
        def solve(number):
            if number >= len(search):
                self.check = True
                return 
            x ,y= search[number]
            for i in range(1,10):
                left = (y//3)
                down = x//3
                down = (down * 3) + 1
                down += left
                if (str(i) in row[x]) or (str(i) in col[y]) or (str(i) in cells[down]):
                    continue
                board[x][y] = str(i)
                cells[down].add(str(i))
                row[x].add(str(i))
                col[y].add(str(i))
                solve(number + 1)
                if not self.check:
                    cells[down].remove(str(i))
                    row[x].remove(str(i))
                    col[y].remove(str(i))
        solve(0)

