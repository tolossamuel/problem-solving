class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        catch = {}
        def solve(sell,buy):
            if sell >= len(prices):
                return 0
            if (sell,buy) in catch:
                return catch[(sell,buy)]
            i = buy if prices[sell] >= prices[buy] else sell
           
            ans = max (
                solve(sell+1,i),
                solve(sell+2,sell+2) + prices[sell] - prices[buy]
            )
            catch[(sell,buy)] = ans

            return ans
        return solve(0,0)