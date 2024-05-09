class Solution:
    def find(self,x):
        if x == self.dic[x]:
            return x
        self.dic[x] = self.find(self.dic[x])
        return self.dic[x]
    def union(self,x,y):
        xp = self.find(x)
        yp = self.find(y)
        if x != y and xp == yp:
            self.ans += [[x,y]]
        if self.size[xp] < self.size[yp]:
            yp,xp = xp, yp
        self.dic[yp] = xp
        self.size[xp] += self.size[yp]
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.dic = {x:x for x in range(1,len(edges)+1)}
        self.size ={x:1 for x in range(1,len(edges)+1)}
        self.ans = []
        for x,y in edges:
            self.union(x,y)
        return self.ans[-1]