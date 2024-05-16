class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max = 0
        catch = {}
        def solve(index,sell):
            if index >= len(prices):
                return 0
            
            if sell == 5:
                return 0
            if (index,sell) in catch:
                return catch[(index,sell)]
            if sell%2 == 0:
                ans = max(
                    -prices[index] + solve(index+1,sell + 1),
                    solve(index+1,sell)
                )
            else:
                ans = max(
                    prices[index] + solve(index+1,sell+1),
                    solve(index+1,sell)
                )
            catch[(index,sell)] = ans
            return ans
        return solve(0,0)

