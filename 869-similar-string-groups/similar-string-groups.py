class Solution:
    def find(self,x):
        if x == self.dic[x]:
            return x
        self.dic[x] = self.find(self.dic[x])
        return self.dic[x]
    def union(self,x,y):
        xparent = self.find(x)
        yparent = self.find(y)
        if self.size[xparent] > self.size[yparent]:
            self.dic[yparent] = xparent
            self.size[xparent] += self.size[yparent]
        else:
            self.dic[xparent] = yparent
            self.size[yparent] += self.size[xparent]
    def check(self,x,y):
        dif = 0
        if len(x) == 1 and x[0] != y[0]:
            return False
        for i in range(min(len(x),len(y))):
            if x[i] != y[i]:
                dif += 1
        
        return dif <= 2
    def numSimilarGroups(self, strs: List[str]) -> int:
        self.dic = {x:x for x in strs}
        self.size = {x:1 for x in strs}
        for i in range(len(strs)):
            for y in range(i,len(strs)):
                if self.check(strs[i],strs[y]):
                    self.union(strs[i],strs[y])
        counter = set()
        print(self.dic)
        for key in self.dic:
            self.find(key)
        for key in self.dic:
            counter.add(self.dic[key])
        return len(counter)