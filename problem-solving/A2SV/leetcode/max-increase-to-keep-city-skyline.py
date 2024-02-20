class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxRow = [0]*len(grid[0])
        maxColumn = [0] * len(grid)
        for i in range(len(grid)):
            for y in range(len(grid[0])):
                maxRow[y] = max(maxRow[y],grid[i][y])
                maxColumn[i] = max(maxColumn[i],grid[i][y])
        _sum = 0
        for i in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[i][y]  < maxRow[y] and grid[i][y] < maxColumn[i]:
                    
                    _sum +=( min(maxRow[y],maxColumn[i]) - grid[i][y])
                    # print(grid[i][y],maxRow[y],maxColumn[i],min(maxRow[y],maxColumn[i])),_sum
        return _sum