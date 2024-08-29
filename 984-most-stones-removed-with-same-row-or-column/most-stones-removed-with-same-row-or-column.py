class Solution:

    def find(self,x):
        if x == self.dic[x]:
            return x
        self.dic[x] = self.find(self.dic[x])
        return self.dic[x]
    def union(self,x,y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x == p_y:
            return 
        if self.size[p_x] < self.size[p_y]:
            p_x,p_y = p_y,p_x
        self.dic[p_y] = self.dic[p_x]
        self.size[p_x] += self.size[p_y]
        self.size[p_y] = 1

    
    def removeStones(self, stones: List[List[int]]) -> int:
        self.dic = {
            tuple(stone) : tuple(stone) for stone in stones
        }
        self.size = {
            tuple(stone) : 1 for stone in stones
        }

        for stone in stones:
            for x in stones:
                if stone[0] == x[0] or stone[1] == x[1]:
                    self.union(tuple(stone),tuple(x))
        for key in self.dic:
            self.find(key)

        ans = 0
        for key in self.size:
            ans += (self.size[key] - 1)
        return ans