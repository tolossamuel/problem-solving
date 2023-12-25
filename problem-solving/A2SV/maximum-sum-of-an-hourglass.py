class Solution(object):
    def maxSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)-2):
            # print(i)
            temp = 0
            for y in range(len(grid[0])):
                # print(y)
                if y <2:
                    temp += (grid[i][y] + grid[i+2][y])                
                else:
                    if y == 2:
                        temp += (grid[i][y] + grid[i+2][y] + grid[i+1][y-1])
                        ans = max(temp,ans)
                    else:
                        ans = max(temp,ans)
                        temp -= (grid[i][y-3]+grid[i+2][y-3] + grid[i+1][y-2])
                        temp +=( grid[i][y] + grid[i+2][y] +  grid[i+1][y-1])
            ans = max(temp,ans)
        return ans