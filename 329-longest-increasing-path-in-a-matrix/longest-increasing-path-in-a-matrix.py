class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dic = defaultdict(list)
        dgree = defaultdict(int)
        def check(x,y):
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                return True
            return False
        for i in range(n):
            for y in range(m):
                for r,c in ((1,0),(-1,0),(0,1),(0,-1)):
                    newi = i+r
                    newy = y+c
                    if check(newi,newy) and (matrix[newi][newy] < matrix[i][y]):
                        dic[(i,y)].append((newi,newy))
                        dgree[(newi,newy)] += 1
        q = deque([])
        for i in range(n):
            for j in range(m):
                if dgree[(i,j)] == 0:
                    q.append((i,j))
        level = 0
        while(q):
            length = len(q)
            for _ in range(length):
                cur = q.popleft()
                for x in dic[cur]:
                    dgree[x] -= 1
                    if dgree[x] == 0:
                        q.append(x)
            level += 1
    
        return level