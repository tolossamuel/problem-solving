class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
     
        def check(x,y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                return True
            return False
        def travel(x,y):
            dic = [(0,1),(0,-1),(-1,0),(1,0)]
            for i, j in dic:
                new_x = x+i
                new_y = y + j
                if check(new_x,new_y) and grid[new_x][new_y] == 0:
                    grid[new_x][new_y] = 2
                    travel(new_x,new_y)
        for i in (0,len(grid)-1):
            for y in range(len(grid[0])):
                if grid[i][y] == 0:
                    grid[i][y] = 2
                    travel(i,y)
        for y in (0,len(grid[0])-1):
            for i in range(len(grid)): 
                if grid[i][y] == 0:
                    grid[i][y] = 2
                    travel(i,y)
        ans = 0
        for i in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[i][y] == 0:
                    grid[i][y] = 2
                    travel(i,y)
                    ans += 1
        return ans