class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        rows, cols, count = len(grid1), len(grid1[0]), 0
        
        def dfs(x, y):
            if x < 0 or x >= rows or y < 0 or y >= cols or grid2[x][y] != 1:
                return
            
            grid2[x][y] = 0
            for i, z in [(0,-1), (0,1), (-1,0), (1,0)]:
                dfs(i+x, z+y)
        
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    dfs(i, j)
                    count += 1
                    
        return count