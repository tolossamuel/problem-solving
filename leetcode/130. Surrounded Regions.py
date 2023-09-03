class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(x , y):
            if board[x][y] == "X":
                return 
            board[x][y] = 'T'
            direction = [(1,0),(0,1),(-1,0),(0,-1)]
            for a,b in direction:
                    if (x + a)>=0 and (y + b) >=0 and (x + a) < len(board) and (y + b) < len(board[0]):
                        if board[x+a][y+b]=='O':
                            dfs(x+a,y+b)
        for i in range(len(board)):
            for y in range(len(board[0])):
                if (i == 0 or i + 1 == len(board)):
                    if board[i][y] == "O":
                        dfs(i, y)
                elif y > 0 and y < len(board[0])-1:
                    continue
                else:
                    if board[i][y] == "O":
                        dfs(i, y)
        for i in range(len(board)):
            for y in range(len(board[0])):
                if board[i][y] == "T":
                    board[i][y] = "O"
                elif board[i][y] == "O":
                    board[i][y] = "X"