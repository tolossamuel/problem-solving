class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        def count(i,y,val):
            nonlocal ans
            ans += val
            grid[i][y] = 2
            for r,c in ((0,1),(-1,0),(1,0),(0,-1)):
                if not (0 <= i + r < len(grid) and 0 <= y + c < len(grid[0]) ):
                    continue
                if grid[i+r][y+c] == 1:
                    ans -= 1
                    count(i+r,y+c,4)
                elif grid[i+r][y+c] == 2:
                    ans -= 1
        for i in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[i][y] == 1:
                    count(i,y,4)
                    break

        return ans