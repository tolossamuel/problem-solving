class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10**9 + 7
        comp = []
        heap = []
        for i in range(len(speed)):
            comp.append([efficiency[i],speed[i]])
        comp.sort(reverse = True)
        ans = float("-inf")
        _sum = 0
        for i in range(len(comp)):
            if k > 0:
                _sum += comp[i][1]
                ans = max(ans,_sum * comp[i][0])
                heappush(heap,(comp[i][1],comp[i][0]))
                k-= 1
                if k == 0:
                    temp = _sum * comp[i][0]
                    ans = max(ans,temp)
            else:
                t,v = heappop(heap)
                _sum -= t
                _sum += comp[i][1]
                heappush(heap,(comp[i][1],comp[i][0]))
                ans = max(ans,_sum *comp[i][0])
        return ans%mod



































