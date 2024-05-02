class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        ans = set()
        for x in range(len(fronts)):
            ans.add((backs[x],fronts[x]))
        val = float("inf")
        for x in backs:
            if (x,x) not in ans:
                val = min(val,x)
        for x in fronts:
            if (x,x) not in ans:
                val = min(val,x)
        return val if val != float("inf") else 0