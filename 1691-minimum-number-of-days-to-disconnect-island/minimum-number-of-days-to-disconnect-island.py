class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        copys = copy.deepcopy(grid)
        island = float("inf")
        visited = []
        counter = 0
        def check(x,y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                return True
            return False
        def dfs(x,y,c):
            nonlocal counter
            nonlocal visited
            dir = [(1,0),(-1,0),(0,-1),(0,1)]
            if grid[x][y] == 1:
                if c == 1:
                    visited.append([x,y])
                grid[x][y] = -1

                counter += 1
            for  i,j in dir:
                nx = x + i
                ny = y + j
                if check(nx,ny) and grid[nx][ny] == 1:
                    dfs(nx,ny,c)
            
        number = 0
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    number += 1
                    dfs(x,y,1)
                    # print(counter)
                    island = min(island,counter)
                    counter = 0

        if number > 1:
            return 0
        elif number == 0:
            return 0
        elif island <= 2:
            return island
        number = 0
        island = float("inf")
        grid = copy.deepcopy(copys)
        counter = 0
        for i in range(len(visited)):
            if i == 0:
                j,k = visited[1][0],visited[1][1]
            else:
                j,k = visited[0][0],visited[0][1]
 
            grid[visited[i][0]][visited[i][1]] = 0
            number += 1
            dfs(j,k,0)
          
            island = min(island,counter)
            grid[visited[i][0]][visited[i][1]] = 0
            counter = 0
            
            
            if island + 1 < len(visited):
                return 1
            grid = copy.deepcopy(copys)
            number = 0
            island = float("inf")
        return 2
            



