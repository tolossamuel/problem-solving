class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        start = defaultdict(int)
        ans = 0
        val = 0
        for i,x in edges:
            start[i] += 1
            start[x] += 1
            if val < start[i]:
                ans = i
                val = start[i]
            if val < start[x]:
                ans = x
                val = start[x]
        return ans
