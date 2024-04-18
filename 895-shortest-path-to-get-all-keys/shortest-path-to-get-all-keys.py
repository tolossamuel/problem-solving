class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        keys = "abcdef"
        start = []
        key_number = 0
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        visited = set()
        def check(x,y):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                return True
            return False
        for i in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[i][y] == "@":
                    start = [[i,y,0,0,".@abcdef"]]
                if grid[i][y] in keys:
                    key_number += 1
        
        start = deque(start)

        while(start):
            x,y,n_k,step,k_v = start.popleft()
            if grid[x][y] in "abcdef" and grid[x][y].upper() not in k_v:
                k_v += grid[x][y].upper()
                n_k += 1
            if n_k == key_number:
                return step
            for i,j in dir:
                nx = x + i
                ny = y + j
                if check(nx,ny) and (nx,ny,k_v) not in visited:
                    if grid[nx][ny] in k_v:
                        visited.add((nx,ny,k_v))
                        start.append((nx,ny,n_k,step + 1,k_v))
        return -1


