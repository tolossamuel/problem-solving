class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        memory = {(len(grid)-1,y): grid[len(grid)-1][y] for y in range(len(grid))}
        ans = float("inf")
        for x in range(len(grid)-2,-1,-1):
            for y in range(len(grid)-1,-1,-1):
                index = x + 1
                val = float("inf")
                for i in range(len(grid)):
                    if i != y:
                    
                        val = min(memory[(index,i)],val)
                memory[(x,y)] = val + grid[x][y]
                
        for x in range(len(grid)):
            ans = min(ans,memory[(0,x)])
  
        return ans
