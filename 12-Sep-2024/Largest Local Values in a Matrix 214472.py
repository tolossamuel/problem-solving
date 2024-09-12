# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        heap = []
        ans = [[0 for i in range(len(grid))] for i in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid)):
                for x in range(i,min(len(grid),i+3)):
                    for y in range(j,min(len(grid),j+3)):
                        ans[i][j] = max(ans[i][j],grid[x][y])
        val = []
        for i in range(len(ans)-2):
            val.append(ans[i][:len(ans)-2])

            
        return val