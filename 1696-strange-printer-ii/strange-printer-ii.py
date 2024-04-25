class Solution:
    def creat(self):
        n = len(self.targetGrid)
        m = len(self.targetGrid[0])
        for i in range(n):
            for y in range(m):
                x1,y1,x2,y2 = self.dic[self.targetGrid[i][y]]
                x1 = min(x1,i)
                y1 = min(y1,y)
                x2 = max(x2,i)
                y2 = max(y2,y)
                self.colors.add(self.targetGrid[i][y])
                self.dic[self.targetGrid[i][y]] = [x1,y1,x2,y2]
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        self.targetGrid = targetGrid
        self.dic = defaultdict(lambda:[float("inf"),float("inf"),float("-inf"),float("-inf")])
        self.colors = set()
        self.creat()
        dependent = defaultdict(list)
        indgree = defaultdict(int)
        for key in self.colors:
            visited = set([key])
            for x in range(self.dic[key][0],self.dic[key][2]+1):
                for y in range(self.dic[key][1],self.dic[key][3]+1):
                    if self.targetGrid[x][y] not in visited:
                        visited.add(self.targetGrid[x][y])
                        dependent[key].append(self.targetGrid[x][y])
                        indgree[self.targetGrid[x][y]] += 1
        q = deque([x for x in self.colors if indgree[x] == 0])
        color = 0
        while(q):
            cur = q.popleft()
            for c in dependent[cur]:
                indgree[c] -= 1
                if indgree[c] == 0:
                    q.append(c)
            color += 1
        return color == len(self.colors)


