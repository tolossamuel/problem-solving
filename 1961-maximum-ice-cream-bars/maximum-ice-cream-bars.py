class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapify(costs)
        counter = 0
        while(costs):
            x = heappop(costs)
            if x > coins:
                return counter
            counter += 1
            coins -= x
        return counter