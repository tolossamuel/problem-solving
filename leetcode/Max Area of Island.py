class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_counter = 0
        counter = 0
        def counter_area(grid, visited, index):
            counter = 0
            if grid[visited][index] != 1:
                return
            grid[visited][index] = 2 #change color
            counter += 1
            direction = [(0,1), (1,0), (0,-1), (-1,0)]
            for i, x in direction: 
                if  visited + i >= 0 and visited + i < len(grid) and index + x >= 0 and index + x < len(grid[0]):
                    if grid[(visited + i)][(index + x)] == 1:
                        counter += counter_area(grid, (visited + i),(index + x)) 
            return counter
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for y in range(m):
                if grid[i][y] == 1:
                    max_counter = max(max_counter, counter_area(grid,i,y))
        return max_counter