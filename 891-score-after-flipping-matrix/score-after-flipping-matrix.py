class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        change = (2**n)-1
        arr = [0] * len(grid[0])
        for i in range(len(grid)):
            if grid[i][0] != 1:
                for j in range(len(grid[0])):
                    grid[i][j] = "0" if grid[i][j] == 1 else "1"
                    if grid[i][j] == "0":
                        arr[j] += 1
            else:
                for j in range(len(grid[0])):
                    grid[i][j] = str(grid[i][j])
                    if grid[i][j] == "0":
                        arr[j] += 1
        ans = 0
        n = len(grid)
        t = 1
        for i in range(len(arr)-1,-1,-1):
            if (n//2 < arr[i]):
                ans += (t * arr[i])
            else:
                ans += (t * (n-arr[i]))
            t *= 2
        return ans
