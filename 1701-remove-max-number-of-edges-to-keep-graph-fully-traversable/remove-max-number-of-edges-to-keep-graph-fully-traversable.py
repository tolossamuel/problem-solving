class Solution:
    def find(self,x):
        if x == self.dic[x]:
            return x
        self.dic[x] = self.find(self.dic[x])
        return self.dic[x]
    def union(self,x,y):
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp:
            self.counter += 1
            return 
        if self.size[xp] < self.size[yp]:
            xp,yp = yp,xp
        self.visited.add(xp)
        self.dic[yp] = xp
        self.size[xp] += self.size[yp]

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse = True)
        m = len(edges)
        self.dic = {x:x for x in range(1,n+1)}
        self.size = {x:1 for x in range(1,n+1)}
        self.visited = set()
        self.counter = 0
        i = 0
        while(i < m and edges[i][0] == 3):
            _,x,y = edges[i]
            self.union(x,y)
            i+= 1
        
        

        temp = self.dic.copy()
        temp2 = self.size.copy()
        while(i < m and edges[i][0] == 2):
            _,x,y = edges[i]
            self.union(x,y)
            i+=1
        for key in self.dic:
            self.find(key)
        c = len(set(list(self.dic.values())))
        if c > 1:
            return -1
        self.dic = temp
        self.size = temp2

        while(i < m and edges[i][0] == 1):
            _,x,y = edges[i]
            self.union(x,y)
            i+= 1
        for key in self.dic:
            self.find(key)
        c = len(set(list(self.dic.values())))
        if c > 1:
            return -1
        return self.counter


