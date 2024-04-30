class Solution:
    def find(self,x):
        if x == self.dic[x]:
            return x
        self.dic[x] = self.find(self.dic[x])
        return self.dic[x]
    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp:
            return 
        if self.size[yp] > self.size[xp]:
            xp,yp = yp,xp
        self.dic[yp] = xp
        self.size[xp] += self.size[yp]
    def check(self,x,y,n,m):
        if 0<= x < n and 0 <= y < m:
            return True
        return False
    def creat(self,x,y,n,m):
        dir = ((0,1),(0,-1),(-1,0),(1,0))
        for i,j in dir:
            nx = x+i
            ny = y + j
            if self.check(nx,ny,n,m) and self.grid[nx][ny] > 0:
                self.union((x,y),(nx,ny))
            
    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.dic = {}
        self.size = {}
        self.grid = grid
        n = len(grid)
        m = len(grid[0])
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] > 0:
                    self.dic[(x,y)] = (x,y)
                    self.size[(x,y)] = 1
       
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] > 0:
                    self.creat(x,y,n,m)
        for key in self.dic:
            self.find(key)
        ans = defaultdict(int)
        _max = 0
        for key in self.dic:
            ans[self.dic[key]] += self.grid[key[0]][key[1]]
            _max = max(_max,ans[self.dic[key]])
        return _max