class Solution:
    def findRotateSteps(self, ring, key):
        
        rLen, kLen, d = len(ring), len(key), defaultdict(list)
        dist = lambda x,y : min((x-y)%rLen, (y-x)%rLen)

        for i, ch in enumerate(ring): d[ch].append(i)

        @lru_cache(None)
        def dfs(curr = 0,next = 0):

            if next >= kLen: return 0

            return min(dist(curr,k)+dfs(k,next+1) for k in d[key[next]])

        return dfs() + kLen