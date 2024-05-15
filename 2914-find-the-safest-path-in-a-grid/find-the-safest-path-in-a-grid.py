class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        arr = [[-1 for _ in range(len(grid[0]))]for _ in range(len(grid))]
        start = deque([])
        for i in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[i][y] == 1:
                    start.append([i,y])
                    arr[i][y] = 0
        dir = ((1,0),(-1,0),(0,1),(0,-1))
        _max = 0
        dis = 1
  
        while(start):
            n = len(start)
            for _ in range(n):
                x,y = start.popleft()
                _max = max(dis,_max)    
                for i,j in dir:
                    nx = x + i
                    ny = y + j
                    if (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) and arr[nx][ny] == -1:
                        start.append([nx,ny])
                        arr[nx][ny] = dis
            dis += 1

        def check(x,y):
            if 0<= x < len(grid) and 0 <= y < len(grid[0]):
                return True
            return False
        # print(arr)
        # def solve(x,y,val):
        #     if x == len(grid)-1 and y == len(grid[0])-1:
        #         return True
        #     re = False
        #     for i,j in dir:
        #         nx = x + i
        #         ny = y + j
        #         if check(nx,ny):
        #             if (arr[nx][ny] >= val):
        #                 v = arr[nx][ny]
        #                 arr[nx][ny] = float("-inf")
        #                 re = re or solve(nx,ny,val)
        #                 arr[nx][ny] = v
        #                 if re:
        #                     return True
        #     return re
        n = len(grid)
        def solve(f,visited, a=0,b=0):
            if a == n-1 and b == n-1:
                return True
            visited[a][b] = True          
            for x,y in dir:
                x,y = x+a,y+b
                if 0 <= x < n and 0 <= y < n and not visited[x][y] and arr[x][y] >= f:
                    if solve(f,visited,x,y):
                        return True
            return False

        left = 0
        right = arr[0][0]
        val = 0
        while(left <= right):
            mid = (left + right)//2
            if solve(mid,[[False] * len(grid) for _ in range(len(grid))]):
                val = max(val,mid)
                left = mid + 1
            else:
                right = mid - 1
            # print(arr)
        return val
