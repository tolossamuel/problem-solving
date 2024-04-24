class Solution:
   
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        dic = defaultdict(list)
        for x,y,v in roads:
            dic[x].append((y,v))
            dic[y].append((x,v))
        q = deque([[1,float("inf")]])
        ans = float("inf")
        visited = set([1])
        while(q):
            cur = q.popleft()
            for x,y in dic[cur[0]]:
                ans = min(ans,y)
                if x not in visited:
                    visited.add(x)
                    q.append([x,y])
        
        return ans



