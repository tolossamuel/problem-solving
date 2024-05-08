class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        ans = w
        heap = []
        comp = []
        for i in range(len(profits)):
            comp.append([capital[i],profits[i]])
        comp.sort()
        index = 0
        while(k):
            while(index < len(comp) and comp[index][0] <= ans ):
                heappush(heap,-comp[index][1])
                index += 1
            if heap:
                ans += -heappop(heap)
            k -= 1
        return ans