class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def rowCol(value):
            r = (value - 1) // n
            c = ((value-1) % n)
            if r % 2 == 1:
                c = n -1 - c
            return (n-1-r,c)
        start = deque([(1,0)])
        visited = set()
        while(start):
            val,dis = start.popleft()
            
            r,c = rowCol(val)
            if board[r][c] != -1:
                val = board[r][c]
            if val == (n*n):
                return dis
            
            for i in range(1,7):
                _new = val + i
                if _new <= (n*n) and (_new) not in visited:
                    visited.add(_new)
                    start.append((_new,dis+1))
        return -1

