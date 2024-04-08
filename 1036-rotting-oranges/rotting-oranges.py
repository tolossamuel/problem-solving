class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = set()
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for y in range(col):
                if grid[i][y] == 2:
                    rotten.append((i,y))
                elif grid[i][y] == 1:
                    fresh.add((i,y))
        counter = 0
        def solve():
            nonlocal rotten, counter, fresh
            if not rotten:
                return 
            temp = deque()
            while(rotten):
                x,y = rotten.popleft()
                rorred = False
                for r,c in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if (0 <= x + r < row and 0 <= y + c < col):
                        if grid[x + r][y + c] == 1:
                            temp.append((x+r,y+c))
                            grid[x + r][y + c] = 2
                            fresh.remove((x + r, y + c))
            if temp:
                counter += 1
            rotten = temp.copy()
            solve()
        solve()
        if not fresh:
            return counter
        return -1

                        
