class Solution:
    def find(self,x):
        if x == self.dic[x]:
            return x
        s = self.find(self.dic[x])
        self.dic[x] = min(self.dic[x],s)
        return self.dic[x]
    def union(self,x,y):
        xparent = self.find(x)
        yparent = self.find(y)
        if xparent < yparent:
            self.dic[yparent] = xparent
        else:
            self.dic[xparent] = yparent
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        self.dic = {x:x for x in (s1+s2)}
        for x in range(len(s1)):
            self.union(s1[x],s2[x])
        ans = []
        for key in self.dic:
            self.find(key)
        for i in baseStr:
            if i in self.dic:
                ans.append(self.dic[i])
            else:
                ans.append(i)
        return "".join(ans)