class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        def check(x,y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                return True
            return False
        dir = ((1,0),(-1,0),(0,1),(0,-1))
        def travel(x,y):
            if not check(x,y):
                return 0
            if grid[x][y] == 0:
                return 0
            val = grid[x][y]
            ans = 0
            grid[x][y] = 0
            for i,j in dir:
                ans = max(ans,val + travel(x+i,y+j))
            grid[x][y] = val
            return ans
            
        ans = 0
        for i in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[i][y] > 0:
                    ans = max(ans,travel(i,y))
       
        
        print(ans)
        return ans
            



            