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
            self.size[xp] += self.size[yp]
            self.dic[yp] = xp
        else:
            self.size[yp] += self.size[xp]
            self.dic[xp] = yp
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key = lambda x : x[2])
        self.dic = {x:x for x in range(n)}
        self.size = {x:1 for x in range(n)}
        proces = [queries[i] + [i] for i in range(len(queries))]
        proces.sort(key = lambda x : x[2])
        left = 0
        right = 0
        ans = [False] * len(queries)
        while(left < len(proces)):
            if right >= len(edgeList) or (edgeList[right][2] >= proces[left][2]):
                p1 = self.find(proces[left][0])
                p2 = self.find(proces[left][1])
                ans[proces[left][3]] = p1 == p2
                left += 1
            else:
                self.union(edgeList[right][0],edgeList[right][1])
                right += 1
        return ans