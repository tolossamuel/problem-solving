class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort(reverse = True)
        you = 0
        n = len(piles)//3
        for i in range(1,n*2, +2):
            you += piles[i]
        return you

            