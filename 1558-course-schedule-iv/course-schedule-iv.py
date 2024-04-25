class Solution:
    def find(self,x):
        while x != self.dic[x]:
            x = self.dic[x]
        return x
    def union(self,x,y):
        yp = self.find(y)
        self.dic[yp] = x
    def validpath(self,x,y):
        while(y != x and y != self.dic[y]):
            y = self.dic[y]
        return x == y
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
                self.dic = defaultdict(list)
                self.dgree = [0] * numCourses
                matrix = [[False for _ in range(numCourses)] for _ in range(numCourses)]
                for x,y in prerequisites:
                    self.dic[y].append(x)
                    self.dgree[x] += 1
                    matrix[x][x] = True
                    matrix[y][y] = True
                
                q = deque([x for x in self.dic if self.dgree[x] == 0])
                while(q):
                    cur = q.popleft()
                    for n in self.dic[cur]:
                        for c in range(len(matrix[cur])):
                            if matrix[cur][c]:
                                matrix[n][c] = True
                        self.dgree[n] -= 1
                        if self.dgree[n] == 0:
                            q.append(n)
                ans = []
                for x,y in queries:
                    ans.append(matrix[x][y])
                return ans