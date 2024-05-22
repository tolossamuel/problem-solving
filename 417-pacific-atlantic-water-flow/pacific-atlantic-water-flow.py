class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = [[[False,False] for _  in range(m) ] for _ in range(n)]
        atlantic = [[[False,False] for _ in range(m) ] for _ in range(n)]
        for i in range(m):
            atlantic[0][i] = [True|atlantic[0][i][0],False|atlantic[0][i][1]]
            atlantic[n-1][i] = [False|atlantic[n-1][i][0],True|atlantic[n-1][i][0]]
        for i in range(n):

            atlantic[i][0] = [True|atlantic[i][0][0],False|atlantic[i][0][1]]
            atlantic[i][m-1] = [False|atlantic[i][m-1][0],True|atlantic[i][m-1][1]]
        def check(x,y):
            if 0 <= x < len(heights) and 0 <= y < len(heights[0]):
                return True
            return False
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(r,c):
            if not check(r,c):
                return [False,False]
            if atlantic[r][c][0] == atlantic[r][c][1] and atlantic[r][c][0] == True:
                return [True,True]
            
            ans = atlantic[r][c]
            for i,j in dir:
                nx = r+i
                ny = c+j

                if not check(nx,ny):
                    continue
                if heights[r][c] >= heights[nx][ny]:
                    val = heights[r][c]
                    heights[r][c] = float("inf")
                    p,o = dfs(nx,ny)
                    ans = [ans[0]|p,ans[1]|o]
                    atlantic[r][c] = ans
                    heights[r][c] = val
                if ans[0] and ans[1]:
                    atlantic[r][c] = ans
                    return ans
            return atlantic[r][c]
        for i in range(n):
            for y in range(m):
                if not atlantic[i][y][0] or not atlantic[i][y][1]:
                    dfs(i,y)
        matrix = []
        for i in range(len(atlantic)):
            for j in range(len(atlantic[i])):
                if atlantic[i][j][0] and atlantic[i][j][1]:
                    matrix.append([i,j])
        return matrix
            