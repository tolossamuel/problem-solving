class Solution:
    def find(self,x):
        if x == self.dic[x]:
            return x

        self.dic[x] = self.find(self.dic[x])
        return self.dic[x]
    def union(self,x,y):
        xp = self.find(x)
        yp = self.find(y)
        if xp == yp or yp != y:
            return 
        self.dic[yp] = xp
    
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        self.dic= {x:x for x in range(n)}
        visited = set()
        ans = 0
        for x,y in edges:
            self.union(x,y)
        for key in self.dic:
            self.find(key)
        for key in self.dic:
            visited.add(self.dic[key])
            ans = self.dic[key]
        if len(visited) > 1:
            return -1
        return ans   