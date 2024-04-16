class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ans = [-x for x in stones]
        heapify(ans)
        while(len(ans) > 1):
            x = -heappop(ans)
            y = -heappop(ans)
            if x == y:
                continue
            else:
                heappush(ans,-(x-y))
        return 0 if not ans else -ans[0]
            