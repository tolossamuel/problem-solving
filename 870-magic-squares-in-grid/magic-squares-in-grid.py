class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def dis(x,y):
            visited = [-1] * 9

            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if 0 < grid[i][j] <= 9:
                        visited[grid[i][j]-1] = grid[i][j]
                    else:
                        return False
            # print(x,y,visited)
            if -1 in visited:
                return False
            return True

        def cal(x,y):
            # print(x,y)
            _sum = grid[x][y-1] + grid[x][y] + grid[x][y+1]
            # print(_sum)
            # [3,2,9,2,7]
            # [6,1,8,4,2]
            # [7,5,3,2,7]
            # [2,9,4,9,6]
            # [4,3,8,2,5]
            dir = (((1,0),(-1,0)),((-1,-1),(1,1)),((-1,1),(1,-1)))
            for i in range(3):
                temp = grid[x][y]
                # print(temp)
                for j,z in dir[i]:
                    temp += grid[x+j][y+z]
                    # print(grid[x+j][y+z],j,z,x,y,x+j,)
                # print(_sum,"===",temp)
                if _sum != temp:
                    return False
                
            dir = (((-1,-1),(1,-1)),((1,-1),(1,1)),((-1,-1),(-1,1)),((-1,1),(1,1)))
            z = 0
            for i,j in ((x,y-1),(x+1,y),(x-1,y),(x,y+1)):
                temp = grid[i][j]
                for r,c in dir[z]:
                    temp += grid[x+r][y+c]
                z += 1
                if temp != _sum:
                    return False
            return True
        ans = 0
        for i in range(1,len(grid)-1):
            for y in range(1,len(grid[0])-1):
                # print(i,y)
                if dis(i,y) and cal(i,y):
                    ans += 1
        return ans




































