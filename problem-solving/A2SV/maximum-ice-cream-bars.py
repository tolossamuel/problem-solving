class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        total = 0
        for i in range(len(costs)):
            total += costs[i]
            if total == coins:
                return i+1
            elif total > coins:
                return i
        return len(costs)