class Solution(object):
    def onesMinusZeros(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        row = [0 for i in range(len(grid))]
        col = [0 for i in range(len(grid[0]))]
        for i in range(len(grid)):  
            for y in range(len(grid[i])):
                if grid[i][y] == 1:
                    row[i] += 1
                    col[y] += 1
        for i in range(len(grid)):
            for y in range(len(grid[0])):
                grid[i][y] = (2*(row[i] + col[y]) - m - n)
        return grid
                
