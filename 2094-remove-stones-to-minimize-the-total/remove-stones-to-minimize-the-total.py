class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-x for x in piles]
        heapq.heapify(heap)
        print(heap)
        while(k > 0):
            k -= 1
            x = -heapq.heappop(heap)
            y = math.floor(x/2)
            # print(x)
            x -= y
            heapq.heappush(heap,-x)

        return -sum(heap)