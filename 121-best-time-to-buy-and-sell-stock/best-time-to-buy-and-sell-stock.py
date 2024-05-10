class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        big_number = 0
        amount = 0
        for i in range(len(prices)-1,-1,-1):
            big_number = max(big_number,prices[i])
            amount = max(amount,big_number - prices[i])


        return amount