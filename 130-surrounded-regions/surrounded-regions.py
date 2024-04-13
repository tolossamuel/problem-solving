class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check(x,y):
            if 0 <= x < len(board) and  0 <= y < len(board[0]):
                return True
            return False
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        zero = set()
        def travel(x,y):
            for i,j in dir:
                new_x = x + i
                new_y = y + j
                if check(new_x,new_y):
                    if board[new_x][new_y] == "O" and (new_x,new_y) not in zero:
                        zero.add((new_x,new_y))
                        travel(new_x,new_y)
        for i in [0,len(board)-1]:
            for y in range(len(board[0])):
                if board[i][y] == "O" and (i,y) not in zero:
                    zero.add((i,y))
                    travel(i,y)
        for y in [0,len(board[0])-1]:
            for i in range(len(board)):
                if board[i][y] == "O" and (i,y) not in zero:
                    zero.add((i,y))
                    travel(i,y)
        for i in range(len(board)):
            for y in range(len(board[0])):
                if (i,y) not in zero:
                    board[i][y] = "X"


