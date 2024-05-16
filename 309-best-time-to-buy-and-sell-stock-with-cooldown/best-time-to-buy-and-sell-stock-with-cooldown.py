class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        catch = {}
        def solve(index,states):
            if index >= len(prices):
                return 0
            if (index,states) in catch:
                return catch[(index,states)]
            ans = 0
            if states:
                ans = max(solve(index+1,states),
                          -prices[index]+solve(index+1,False))
            else:
                ans = max(
                    solve(index+1,states),
                    prices[index] + solve(index+2,True)
                )
            catch[(index,states)] = ans
            return ans
        return solve(0,True)