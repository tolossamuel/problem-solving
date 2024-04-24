class Solution:
    def find(self,x):
        if x == self.dic[x]:
            return x
        self.dic[x] = self.find(self.dic[x])
        return self.dic[x]
    def union(self,x,y):
        xp = self.find(x)
        yp = self.find(y)
        if self.size[xp] > self.size[yp]:
            self.dic[yp] = xp
            self.size[xp] += self.size[yp]
        else:
            self.dic[xp] = yp
            self.size[yp] += self.size[xp]
    def check(self,x,y):
        if x[0] == y[0] or x[1] == y[1]:
            return True
        
        return False
    def removeStones(self, stones: List[List[int]]) -> int:
        self.dic = {(x[0],x[1]) : tuple(x) for x in stones}
        self.size = {(x[0],x[1]):1 for x in stones}
        for i in range(len(stones)):
            for y in range(i,len(stones)):
                if self.check(stones[i],stones[y]):
                    self.union(tuple(stones[i]),tuple(stones[y]))
        for key in self.dic:
            self.find(key)
        counter = defaultdict(int)
        _max = 0
        for key in self.dic:
            counter[self.dic[key]] += 1
        for key in counter:
            _max += (counter[key]-1)
        return  _max